import re

from . import regist
from . import pyson
from antlr4 import *
from pyson.error import TransformWrongError
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

class DotDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        self.__dict__ = self

def make_filting(content,checker,filter_list=None):
    # the following has this conditions
    # if unlimit is ture, it not influence the checker and the content
    # we just remove the key in filter and the content
    # the first condition is that the cut checker matchs the cut content
    # the second condition is that the origin checker matchs the origin content
    # the first condition is better
    # 
    pattern=r'^[A-Za-z_]+([A-Za-z0-9_])*$'
    for element in filter_list:
        if(re.match(pattern,element) is None):
            raise RuntimeError("The "+element+" is not a key")
    
    content_dict=content.value
    if(not isinstance(content_dict,dict)):
        raise RuntimeError("The filter operation is just for the dict")

    #begin make filting
    #the content
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
            return (self.reg.load_package_object(object_name),None)
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
    def _transform_list(self,content,raw_dict,current_store,root_store,location="",checker=None):
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
                    obj_checker._check_before(current_list[i],raw_dict,location)
                current_store.append(current_list[i].value)
                if(obj_checker is not None):
                    obj_checker._check_after(current_store[i],root_store)
                continue
            if(isinstance(current_list[i].value,pyson.pyson_object.pyson_object)):
                store=[]
                self._transform_object(current_list[i],raw_dict,store,root_store,current_location,obj_checker)
                current_store.append(store[0])
                continue
            if(isinstance(current_list[i].value,list)):
                store=[]
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.element_checker
                current_store.append(store)
                self._transform_list(current_list[i],raw_dict,store,root_store,current_location,obj_checker)
                continue
            if(isinstance(current_list[i].value,dict)):
                store=DotDict()
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.element_checker
                current_store.append(store)
                self._transform_dict(current_list[i],raw_dict,store,root_store,current_location,obj_checker)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)

    def _transform_dict(self,content,raw_dict,current_store,root_store,location="",checker=None):
        current_dict=content.value
        if(checker is not None):
            if(isinstance(checker,dict)):
                from . import checker as ck
                checker=ck.DictChecker(checker)
            checker._check_before(content,raw_dict,location)
        for key,value in current_dict.items():
            #set error location
            current_location=location
            current_location=current_location+"."+str(key)
            #get the checker
            obj_checker=None
            if(checker is not None):
                obj_checker=checker.checker_dict[key]
            #check the type
            if(isinstance(current_dict[key].value,(int,float,bool,str,type(None)))):
                if(obj_checker is not None):
                    obj_checker._check_before(current_dict[key],raw_dict,location)
                current_store[key]=value.value
                if(obj_checker is not None):
                    obj_checker._check_after(current_store[key],root_store)
                continue
            if(isinstance(current_dict[key].value,pyson.pyson_object.pyson_object)):
                store=[]
                self._transform_object(current_dict[key],raw_dict,store,root_store,current_location,obj_checker)
                current_store[key]=store[0]
                continue
            if(isinstance(current_dict[key].value,list)):
                store=[]
                current_store[key]=store
                if(isinstance(obj_checker,str)):
                    print(checker.checker_dict)
                self._transform_list(current_dict[key],raw_dict,store,root_store,current_location,obj_checker)
                continue
            if(isinstance(current_dict[key].value,dict)):
                store=DotDict()
                current_store[key]=store
                self._transform_dict(current_dict[key],raw_dict,store,root_store,current_location,obj_checker)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)


    def _transform_object(self,content,raw_dict,current_store,root_store,location="",checker=None):
        pyson_object=content.value
        if(checker is not None):
            checker._check_before(content,raw_dict,location)
        if(pyson_object.object_name=="" and pyson_object.scope=="self"):
            current_store.append(root_store)
            return
        obj_class=self._get_object(pyson_object.object_name,pyson_object.scope,root_store)
        if(obj_class is None):
            raise TransformWrongError("The "+pyson_object.object_name+" can not be found",
        location,content.line,content.column)
        if(pyson_object.scope=="self" and pyson_object.params is not None):
            raise TransformWrongError("The self object can't be called",
        location,content.line,content.column)
        if(pyson_object.params is None):
            current_store.append(obj_class[0])
            return
        #if the pyson_object.params is not none then check the obj_class[1]
        if(isinstance(pyson_object.params.value,dict)):
            params={}
            self._transform_dict(pyson_object.params,raw_dict,params,root_store,location+"#params",obj_class[1])
            #if the params is wrong throw the exception
            try:
                obj=obj_class[0](**params)
                current_store.append(obj)
            except:
                raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
                location,content.line,content.column)
            return
        if(isinstance(pyson_object.params.value,list)):
            if(obj_class[1] is None):
                params_list=[]
                self._transform_list(pyson_object.params,raw_dict,params_list,root_store,location+"#params",None)
                try:
                    obj=obj_class[0](*params_list)
                    current_store.append(obj)
                except:
                    print(params_list)
                    raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
                    location,content.line,content.column)
                return
            else:
                #special case for the params_list ,first it should be transformed in to dict
                params_list=pyson_object.params.value
                dict_checker=obj_class[1]
                scheme=dict_checker.checker_dict
                scheme_keys=list(scheme.keys())
                if(len(params_list)>len(scheme_keys)):
                    raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
                    location,content.line,content.column)
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
                except:
                    raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
                    location,content.line,content.column)
                return
        if(checker is not None):
            checker._check_after(pyson_object,root_store)


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
    #time consuming
    tree=parser.entry_point()
    ####
    listener=pyson.pysonListener.pysonListener()
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    content=listener.return_value
    
    if(filter_list is not None):
        content,checker=make_filting(content,checker,filter_list)
    result=trans.transfrom(content,checker)
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
    result=trans.transfrom(d,checker)
    result=trans.transfrom(d,checker)
    return result

