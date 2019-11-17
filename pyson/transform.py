import re

from . import regist
from . import pyson
from antlr4 import *
from pyson.error import CheckWrongError
from pyson.error import TransformWrongError
from pyson.error import PysonSyntaxError
from pyson.error import SyntaxErrorListener

#The translated pyson object contain two element,The first one is origin element and the second one is the translated element
#The origin object and the corresponding checker pass to the function call the function first check the origin object and call the function to build the traslated element 
#after the translated element is build it call the checker to check the value and return the translated element
#For the dict checker the dict type check is also called and then call the transform dict and then call the value check 
#In detail for a function, First call the current function check method and then call the function object generate method, then call the function object check method

def intable(content):
    try:
        int(content)
        return True
    except:
        return False

def dict_warper(checker):
    if(isinstance(checker,dict)):
        from . import checker as ck
        checker=ck.DictChecker(checker)
    return checker

class DotDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        self.__dict__ = self

def make_filting(content,checker,filter_list=None):
    pattern=r'^[A-Za-z_]+([A-Za-z0-9_])*$'
    for element in filter_list:
        if(re.match(pattern,element) is None):
            raise RuntimeError("The "+element+" is not a key")
    
    content_dict=content.value
    if(not isinstance(content_dict,dict)):
        raise RuntimeError("The filter operation is just for the dict")

    key_list=list(content_dict.keys())
    for key in key_list:
        if(key not in filter_list):
            del content_dict[key]
    
    if(checker is None):
        return content,checker
    
    from . import checker as ck
    checker_dict=None
    if(isinstance(checker,dict)):
        checker_dict=checker
    else:
        if(not isinstance(checker,ck.DictChecker)):
            raise RuntimeError("The checker is not the instance of DictChecker")
        else:
            checker_dict=checker.checker_dict  
    #the checker
    new_dict={}
    key_list=list(checker_dict.keys())
    for key in key_list:
        if(key in filter_list):
            new_dict[key]=checker_dict[key]
    new_checker=None
    if(isinstance(checker,dict)):
        new_checker=ck.DictChecker(new_dict,[],False,False)
    else:
        new_checker=ck.DictChecker(new_dict,checker.optional,checker.unlimit,checker.allow_none)
    return content,new_checker

class Transformer(object):
    def __init__(self,reg):
        self.reg=reg
    
    def _get_object(self,object_name,scope,root_store):
        if(scope=="name"):
            return self.reg.get_object(object_name)
        if(scope=="import"):
            pack_obj=self.reg.load_package_object(object_name)
            if(pack_obj is None):
                return None
            return (pack_obj,None)
        if(scope=="self"):
            object_name=object_name.split('.')
            current_node=root_store
            for i in range(0,len(object_name)):
                if(intable(object_name[i])):
                    if(isinstance(current_node,list)):
                        if(int(object_name[i])>=len(current_node)):
                            return None
                        current_node=current_node[int(object_name[i])]
                        continue
                    else:
                        return None
                else:
                    if(isinstance(current_node,dict)):
                        if(object_name[i] in current_node.keys()):
                            current_node=current_node[object_name[i]]
                            continue
                        else:
                            return None
                return False
            return (current_node,None)
    
    #current_list is the current_untransformed note,current_store is the filling store
    #root_store is the root of the ctx  
    #row_dict is also should be used for checker input
    #the checker is also important
    #transform list is totally the mass
    def _transform_list(self,content,raw_dict,current_store,root_store,location="",checker=None,instance=True):
        checker=dict_warper(checker)
        current_list=content.value
        if(checker is not None):
            checker._check_before(content,raw_dict,location)
        #get the obj_checker
        obj_checker=None
        if(checker is not None):
            obj_checker=checker.element_checker
        for i in range(0,len(current_list)):
            #set current location
            current_location=location
            current_location=current_location+"."+str(i)
            #checker the type
            if(isinstance(current_list[i].value,(int,float,bool,str,type(None)))):
                if(obj_checker is not None):
                    obj_checker._check_before(current_list[i],raw_dict,current_location)
                if(instance):
                    current_store.append(current_list[i].value)
                if(obj_checker is not None):
                    obj_checker._check_after(current_store[i],root_store)
                continue
            if(isinstance(current_list[i].value,pyson.pyson_object.pyson_object) and current_list[i].value.scope!="self"):
                if(instance):
                    store=[]
                    self._transform_object(current_list[i],raw_dict,store,root_store,current_location,obj_checker,instance)
                    current_store.append(store[0])
                else:
                    self._transform_object(current_list[i],raw_dict,[current_store[i]],root_store,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,pyson.pyson_object.pyson_object) and current_list[i].value.scope=="self"):
                if(instance):
                    store=[]
                    self._transform_self(current_list[i],raw_dict,store,root_store,current_location,obj_checker,instance)
                    current_store.append(store[0])
                else:
                    self._transform_self(current_list[i],raw_dict,[current_store[i]],root_store,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,list)):
                if(instance):
                    store=[]
                    current_store.append(store)
                    self._transform_list(current_list[i],raw_dict,store,root_store,current_location,obj_checker,instance)
                else:
                    self._transform_list(current_list[i],raw_dict,[current_store[i]],root_store,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,dict)):
                if(instance):
                    store=DotDict()
                    current_store.append(store)
                    self._transform_dict(current_list[i],raw_dict,store,root_store,current_location,obj_checker,instance)
                else:
                    self._transform_dict(current_list[i],raw_dict,current_store[i],root_store,current_location,obj_checker,instance)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)

    def _transform_dict(self,content,raw_dict,current_store,root_store,location="",checker=None,instance=True):
        checker=dict_warper(checker)
        current_dict=content.value
        if(checker is not None):
            checker._check_before(content,raw_dict,location)
        for key,value in current_dict.items():
            #set error location
            current_location=location
            current_location=current_location+"."+str(key)
            #get the checker
            obj_checker=None
            if(checker is not None):
                if(key in checker.checker_dict.keys()):
                    obj_checker=checker.checker_dict[key]
            #check the type
            if(isinstance(current_dict[key].value,(int,float,bool,str,type(None)))):
                if(obj_checker is not None):
                    obj_checker._check_before(current_dict[key],raw_dict,current_location)
                if(instance):
                    current_store[key]=value.value
                if(obj_checker is not None):
                    obj_checker._check_after(current_store[key],root_store)
                continue
            if(isinstance(current_dict[key].value,pyson.pyson_object.pyson_object) and current_dict[key].value.scope!="self"):
                if(instance):
                    store=[]
                    self._transform_object(current_dict[key],raw_dict,store,root_store,current_location,obj_checker,instance)
                    current_store[key]=store[0]
                else:
                    self._transform_object(current_dict[key],raw_dict,[current_store[key]],root_store,current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,pyson.pyson_object.pyson_object) and current_dict[key].value.scope=="self"):
                if(instance):
                    store=[]
                    self._transform_self(current_dict[key],raw_dict,store,root_store,current_location,obj_checker,instance)
                    current_store[key]=store[0]
                else:
                    self._transform_self(current_dict[key],raw_dict,[current_store[key]],root_store,current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,list)):
                if(instance):
                    store=[]
                    current_store[key]=store
                    self._transform_list(current_dict[key],raw_dict,store,root_store,current_location,obj_checker,instance)
                else:
                    self._transform_list(current_dict[key],raw_dict,[current_store[key]],current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,dict)):
                if(instance):
                    store=DotDict()
                    current_store[key]=store
                    self._transform_dict(current_dict[key],raw_dict,store,root_store,current_location,obj_checker,instance)
                else:
                    self._transform_dict(current_dict[key],raw_dict,current_store[key],current_location,obj_checker,instance)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)


    def _transform_object(self,content,raw_dict,current_store,root_store,location="",checker=None,instance=True):
        checker=dict_warper(checker)
        pyson_object=content.value
        if(checker is not None):
            checker._check_before(content,raw_dict,location)
        if(instance):
            obj_class=self._get_object(pyson_object.object_name,pyson_object.scope,root_store)
            if(obj_class is None):
                print_obj_name=pyson_object.object_name
                if(pyson_object.scope=="name"):
                    print_obj_name="@"+print_obj_name
                raise TransformWrongError("The object '"+print_obj_name+"' can not be found",
            location,content.line,content.column)
            if(pyson_object.params is None):
                current_store.append(obj_class[0])
                if(checker is not None):
                    checker._check_after(current_store[0],root_store)
                return
            #if the pyson_object.params is not none then check the obj_class[1]
            if(isinstance(pyson_object.params.value,dict)):
                params={}
                self._transform_dict(pyson_object.params,raw_dict,params,root_store,location+"#params",obj_class[1],instance)
                #if the params is wrong throw the exception
                obj=None
                try:
                    obj=obj_class[0](**params)
                    current_store.append(obj)
                except Exception as e:
                    raise TransformWrongError("The params for object '"+pyson_object.object_name+"' is wrong",
                    location,content.line,content.column,obj_class[0].__name__+": "+str(e))
                if(checker is not None):
                    checker._check_after(current_store[0],root_store)
                return
            if(isinstance(pyson_object.params.value,list)):
                if(obj_class[1] is None):
                    params_list=[]
                    self._transform_list(pyson_object.params,raw_dict,params_list,root_store,location+"#params",None)
                    try:
                        obj=obj_class[0](*params_list)
                        current_store.append(obj)
                    except Exception as e:
                        raise TransformWrongError("The params for object '"+pyson_object.object_name+"' is wrong",
                        location,content.line,content.column,obj_class[0].__name__+": "+str(e))
                    if(checker is not None):
                        checker._check_after(current_store[-1],root_store)
                    return
                else:
                    #special case for the params_list ,first it should be transformed in to dict
                    params_list=pyson_object.params.value
                    dict_checker=obj_class[1]
                    scheme=dict_checker.checker_dict
                    scheme_keys=list(scheme.keys())
                    if(len(params_list)>len(scheme_keys)):
                        raise TransformWrongError("The params for object '"+pyson_object.object_name+"' is wrong",
                        location,content.line,content.column," The params in list more than the params in checker define")
                    new_dict={}
                    for i in range(0,len(params_list)):
                        key=scheme_keys[i]
                        new_dict[key]=params_list[i]
                    content.value.params=new_dict
                    params_content=pyson.pyson_object.content(dict,new_dict,content.element_number,content.line,content.column)
                    params_dict={}
                    self._transform_dict(params_content,raw_dict,params_dict,root_store,location+"#params",dict_checker)
                    try:
                        obj=obj_class[0](**params_dict)
                        current_store.append(obj)
                    except Exception as e:
                        raise TransformWrongError("The params for object '"+pyson_object.object_name+"' is wrong",
                        location,content.line,content.column,obj_class[0].__name__+": "+str(e))
                    if(checker is not None):
                        checker._check_after(current_store[0],root_store)
                    return
        else:
            if(checker is not None):
                checker._check_after(current_store[0],root_store)

    def _transform_self_check(self,content,raw_dict,current_store,root_store,location="",checker=None):
        checker=dict_warper(checker)
        obj=content.value
        if(isinstance(obj,(int,float,bool,str,type(None)))):
            if(checker is not None):
                checker._check_before(content,raw_dict,location)
                checker._check_after(content.value,root_store)
            return 
        if(isinstance(obj,pyson.pyson_object.pyson_object) and obj.scope!="self"):
            self._transform_object(content,raw_dict,[current_store],root_store,location,checker,False)
            return
        if(isinstance(obj,list)):
            self._transform_list(content,raw_dict,current_store,root_store,location,checker,False)
            return
        if(isinstance(obj,dict)):
            self._transform_dict(content,raw_dict,current_store,root_store,location,checker,False)
            return
        raise RuntimeError("No possible condition")


    def _index_item(self,index_string,raw_dict,root_store):
        if(index_string==""):
            return root_store,raw_dict,"self."+index_string
        indexs=index_string.split(".")
        current_indexing=root_store
        for index in indexs:
            if(intable(index)):
                if(isinstance(current_indexing,list)):
                    current_indexing=current_indexing[int(index)]
                else:
                    return None
            else:
                if(isinstance(current_indexing,dict)):
                    current_indexing=current_indexing[index]
                else:
                    return None
        transformed_data=current_indexing
        #current indexing is the data
        #then find the index for raw_dict
        current_indexing=raw_dict
        for index in indexs:
            if(intable(index)):
                current_indexing=current_indexing.value[int(index)]
            else:
                current_indexing=current_indexing.value[index]
        raw_data=current_indexing
        if(isinstance(raw_data,pyson.pyson_object.pyson_object) and raw_data.scope=="self"):
            return self._index_item(raw_data.pyson_name,raw_dict,root_store)
        else:
            return transformed_data,raw_data,"self."+index_string
  
    def _transform_self(self,content,raw_dict,current_store,root_store,location="",checker=None,instance=True):
        pyson_object=content.value
        if(pyson_object.params is not None):
            raise TransformWrongError("The self object can not be called",location,content.line,content.column)
        result=self._index_item(pyson_object.object_name,raw_dict,root_store)
        if(result is None):
            raise TransformWrongError("Can not find the self."+pyson_object.object_name,location,content,content.line,content.column)
        transformed_data,raw_data,prev_location=result
        error_accure=False
        reason=None
        try:
            self._transform_self_check(raw_data,raw_dict,transformed_data,root_store,prev_location,checker)
        except Exception as e:
            error_accure=True
            reason=str(e)
            # raise e
        if(error_accure):
            raise TransformWrongError("The 'self."+pyson_object.object_name+"' is wrong",
                        location,content.line,content.column,reason)
        if(isinstance):
            current_store.append(transformed_data)

    def transfrom(self,content,checker=None,dict_filter=[]):
        if(isinstance(content.value,dict)):
            root_store=DotDict()
            current_store=root_store
            self._transform_dict(content,content,current_store,root_store,"self",checker)
            return root_store
        if(isinstance(content.value,list)):
            root_store=[]
            current_store=root_store
            self._transform_list(content,content,current_store,root_store,"self",checker)
            return root_store
        else:
            return None

            

reg=regist.reg
trans=Transformer(reg)

def from_file(file_name,checker_name=None,filter_list=None):
    checker=None
    if(checker_name is not None):
        checker=reg.get_checker(checker_name)
        if(checker is None):
            raise RuntimeError("The "+str(checker_name)+" can not be found")
    input=FileStream(file_name,encoding='utf-8')
    lexer=pyson.pysonLexer.pysonLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(SyntaxErrorListener())
    token_stream=CommonTokenStream(lexer)
    parser=pyson.pysonParser.pysonParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())
    error_accure=False
    try:
        tree=parser.entry_point()
    except SyntaxError as e:
        error_accure=True
        error_msg=str(e)
    if(error_accure):
        e=PysonSyntaxError(error_msg)
        raise e
    listener=pyson.pysonListener.pysonListener()
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    content=listener.return_value

    if(filter_list is not None):
        content,checker=make_filting(content,checker,filter_list)
    try:
        result=trans.transfrom(content,checker)
    except (TransformWrongError,CheckWrongError) as e:
        error_accure=True
        error_msg=str(e)
        error_type=e.__class__
    if(error_accure):
        e=error_type()
        e.set_msg(error_msg)
        raise e
    return result

def from_string(pyson_string,checker_name=None,filter_list=None):
    checker=None
    if(checker_name is not None):
        checker=reg.get_checker(checker_name)
        if(checker is None):
            raise RuntimeError("The "+str(checker_name)+" can not be found")
    input=InputStream(pyson_string)
    lexer=pyson.pysonLexer.pysonLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(SyntaxErrorListener())
    token_stream=CommonTokenStream(lexer)
    parser=pyson.pysonParser.pysonParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())
    tree=parser.entry_point()
    listener=pyson.pysonListener.pysonListener()
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    content=listener.return_value
    if(filter_list is not None):
        content,checker=make_filting(content,checker,filter_list)
    result=trans.transfrom(content,checker)
    return result

