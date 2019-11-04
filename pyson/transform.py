from . import regist
from . import pyson
from antlr4 import *
from collections import OrderedDict
from pyson.error import TransformWrongError



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


def obj_creater(pyson_dict,root_object=None,root_dict_id=None):
    if(root_dict_id==id(pyson_dict)):
        return root_object
    if(root_dict_id is None):
        root_dict_id=id(pyson_dict)
    if(isinstance(pyson_dict,list)):
        return_list=[]
        if(root_object is None):
            root_object=return_list
        for i in range(0,len(pyson_dict)):
            return_list.append(obj_creater(pyson_dict[i],root_object,root_dict_id))
        return return_list
    if(isinstance(pyson_dict,dict)):
        current_obj=obj()
        if(root_object is None):
            root_object=current_obj
        current_obj.init(pyson_dict,current_obj,root_dict_id)
        return current_obj
    return pyson_dict


class obj(object):
    def __init__(self):
        pass

    def init(self, d,root_object=None,root_dict_id=None):
        for a, b in d.items():
            setattr(self, a,obj_creater(b,root_object,root_dict_id))
        
    def _extract_obj_string(self,prefix,value,stored_dict,root_id=None):
        if(root_id==id(value)):
            stored_dict[prefix]=("ctx","ctx")
            return
        if(root_id is None):
            root_id=id(self)
        if(value is None):
            stored_dict[prefix]=None
            return
        if(isinstance(value,obj)):
            for key,v in vars(value).items():
                self._extract_obj_string(prefix+"."+str(key),v,stored_dict,root_id)
            return
        if(isinstance(value,list)):
            for i in range(0,len(value)):
                self._extract_obj_string(prefix+"["+str(i+1)+"]",value[i],stored_dict,root_id)
            return
        if(isinstance(value,(int,float,bool,str))):
            stored_dict[prefix]=value
        else:
            stored_dict[prefix]=(type(value),str(value))

    def __str__(self):
        stored_dict={}
        output_string=""
        self._extract_obj_string("self",self,stored_dict)
        for key,value in stored_dict.items():
            output_string+=key
            if(isinstance(value,tuple)):
                output_string+=": ("
                output_string+=str(value[0])+","+str(value[1])+")\n"
            else:
                output_string+=": "+str(value)
                output_string+="\n"
        return output_string
    


class transformer(object):
    def __init__(self,reg):
        self.reg=reg
    
    def _get_object(self,object_name,scope,root_store):
        if(scope!="self"):
            return self.reg.get_object(object_name,scope)
        else:
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
    def _transform_list(self,current_list,raw_dict,current_store,root_store,location="",checker=None):
        current_list=current_list.value
        if(checker is not None):
            checker._check_before(current_list,raw_dict)
        for i in range(0,len(current_list)):
            if(isinstance(current_list[i].value,(int,float,bool,str))):
                current_store.append(current_list[i].value)
                continue
            if(isinstance(current_list[i].value,pyson.pyson_object.pyson_name)):
                current_store.append(current_list[i].value)
                continue
            if(current_list[i].value is None):
                current_store.append(None)
                continue
            if(isinstance(current_list[i].value,pyson.pyson_object.pyson_object)):
                store=[]
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.element_checker
                self._transform_object(current_list[i],raw_dict,store,root_store,location+"["+str(i)+"]",obj_checker)
                current_store.append(store[0])
                continue
            if(isinstance(current_list[i].value,list)):
                store=[]
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.element_checker
                current_store.append(store)
                self._transform_list(current_list[i],raw_dict,store,root_store,location+"["+str(i)+"]",obj_checker)
                continue
            if(isinstance(current_list[i].value,dict)):
                store={}
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.element_checker
                current_store.append(store)
                self._transform_dict(current_list[i],raw_dict,store,root_store,location+"["+str(i)+"]",obj_checker)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)

    def _transform_dict(self,current_dict,raw_dict,current_store,root_store,location="",checker=None):
        current_dict=current_dict.value
        if(checker is not None):
            checker._check_before(current_dict,raw_dict)
        for key,value in current_dict.items():
            if(isinstance(current_dict[key].value,(int,float,bool,str))):
                current_store[key]=value.value
                continue
            if(current_dict[key].value is None):
                current_store[key]=None
                continue
            if(isinstance(current_dict[key].value,pyson.pyson_object.pyson_name)):
                current_store[key]=current_dict[key].value
                continue
            if(isinstance(current_dict[key].value,pyson.pyson_object.pyson_object)):
                store=[]
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.scheme[key]
                self._transform_object(current_dict[key],raw_dict,store,root_store,location+"."+str(key),obj_checker)
                current_store[key]=store[0]
                continue
            if(isinstance(current_dict[key].value,list)):
                store=[]
                current_store[key]=store
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.scheme[key]
                self._transform_list(current_dict[key],raw_dict,store,root_store,location+"."+str(key),obj_checker)
                continue
            if(isinstance(current_dict[key].value,dict)):
                store={}
                current_store[key]=store
                obj_checker=None
                if(checker is not None):
                    obj_checker=checker.scheme[key]
                self._transform_dict(current_dict[key],raw_dict,store,root_store,location+"."+str(key),obj_checker)
                continue
        if(checker is not None):
            checker._check_after(current_store,root_store)


    def _transform_object(self,pyson_object,raw_dict,current_store,root_store,location="",checker=None):
        origin_pyson_object=pyson_object
        pyson_object=pyson_object.value
        if(checker is not None):
            checker._check_before(pyson_object,raw_dict)
        if(pyson_object.object_name=="ctx"):
            current_store.append(root_store)
            return
        obj_class=self._get_object(pyson_object.object_name,pyson_object.scope,root_store)
        if(obj_class is None):
            raise TransformWrongError("The "+pyson_object.object_name+" can not be found",
        location,origin_pyson_object.line,origin_pyson_object.column)
        if(pyson_object.scope=="self" and pyson_object.params is not None):
            raise TransformWrongError("The self scope object can't be called",
        location,origin_pyson_object.line,origin_pyson_object.column)
        if(pyson_object.params is None):
            current_store.append(obj_class[0])
            return
        #if the pyson_object.params is not none then check the obj_class[1]
        try:
            if(isinstance(pyson_object.params.value,dict)):
                params={}
                self._transform_dict(pyson_object.params,raw_dict,params,root_store,location,obj_class[1])
                obj=obj_class[0](**params)
                current_store.append(obj)
                return
            if(isinstance(pyson_object.params.value,list)):
                if(obj_class[1] is None):
                    params_list=[]
                    self._transform_list(pyson_object.params,raw_dict,params_list,root_store,location,None)
                    obj=obj_class[0](*params_list)
                    current_store.append(obj)
                    return
                else:
                    #special case for the params_list ,first it should be transformed in to dict
                    params_list=pyson_object.params.value
                    checker_dict=obj_class[1]
                    scheme=checker_dict.scheme
                    scheme_keys=list(scheme.key())
                    if(len(params_list)>len(scheme_keys)):
                        raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
        location,origin_pyson_object.line,origin_pyson_object.column)
                    new_dict=OrderedDict()
                    for i in range(0,len(scheme_keys)):
                        key=scheme_keys[i]
                        new_dict[key]=params_list[i]
                    origin_pyson_object.value.params=new_dict
                    self._transform_dict(origin_pyson_object,raw_dict,params_list,root_store,location,scheme)
                    obj=obj_class[0](*params_list)
                    current_store.append(obj)
                    return
        except:
            raise TransformWrongError("The params for object "+pyson_object.object_name+" is wrong",
        location,origin_pyson_object.line,origin_pyson_object.column)
        if(checker is not None):
            checker._check_after(pyson_object,root_store)


    def transfrom(self,pyson_obj,checker=None):
        if(isinstance(pyson_obj.value,dict)):
            print("in")
            root_store={}
            current_store=root_store
            self._transform_dict(pyson_obj,pyson_obj,current_store,root_store,"",checker)
            return root_store
        if(isinstance(pyson_obj.value,list)):
            root_store=[]
            current_store=root_store
            self._transform_list(pyson_obj,pyson_obj,current_store,root_store,"",checker)
            return root_store
        else:
            return None

            

reg=regist.reg
trans=transformer(reg)

def from_file(file_name,checker=None):
    input=FileStream(file_name,encoding='utf-8')
    lexer=pyson.pysonLexer.pysonLexer(input)
    token_stream=CommonTokenStream(lexer)
    parser=pyson.pysonParser.pysonParser(token_stream)
    tree=parser.entry_point()
    listener=pyson.pysonListener.pysonListener()
    # tree_str=tree.toStringTree(recog=parser)
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    d=listener.return_value
    result=trans.transfrom(d,checker)
    return result

def from_string(pyson_string,checke=None):
    input=InputStream(pyson_string)
    lexer=pyson.pysonLexer.pysonLexer(input)
    token_stream=CommonTokenStream(lexer)
    parser=pyson.pysonParser.pysonParser(token_stream)
    tree=parser.entry_point()
    listener=pyson.pysonListener.pysonListener()
    walker=ParseTreeWalker()
    walker.walk(listener,tree)
    d=listener.return_value
    result=trans.transfrom(d,checker)
    return result

def to_object(pyson_dict):
    return obj_creater(pyson_dict)


