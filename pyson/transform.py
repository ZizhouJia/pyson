import re
from inspect import isfunction

from . import regist
from . import pyson
from antlr4 import *
from pyson.error import CheckWrongError
from pyson.error import TransformWrongError
from pyson.error import PysonSyntaxError
from pyson.error import SyntaxErrorListener

import pyson.checker as c

#The translated pyson object contain two element,The first one is origin element and the second one is the translated element
#The origin object and the corresponding checker pass to the function call the function first check the origin object and call the function to build the traslated element 
#after the translated element is build it call the checker to check the value and return the translated element
#For the dict checker the dict type check is also called and then call the transform dict and then call the value check 
#In detail for a function, First call the current function check method and then call the function object generate method, then call the function object check method

def pyson_deep_copy(obj,obj_id,root_id,output_obj=None,output_root=None):
    #if the current is a object just return
    if(isinstance(obj,(int,float,bool,type(None)))):
        return obj
    if(isinstance(obj,str)):
        return "".join(obj)
    if(not isinstance(obj,(dict,list))):
        return obj
    #the first condition, the node is the root
    current_handle=None
    if(obj_id==root_id):
        if(isinstance(obj,dict)):
            output_obj={}
            output_root=output_obj
        if(isinstance(obj,list)):
            output_obj=[]
            output_root=output_obj
        current_handle=output_obj
    else:
        if(id(obj)==root_id):
            if(output_root is not None):
                return output_root
            else:
                if(isinstance(obj,dict)):
                    output_root={}
                if(isinstance(obj,list)):
                    output_root=[]
            current_handle=output_root
        if(id(obj)==obj_id):
            if(output_obj is not None):
                return output_obj
            else:
                if(isinstance(obj,dict)):
                    output_obj={}
                if(isinstance(obj,list)):
                    output_obj=[]
            current_handle=output_obj
    
    if(current_handle is None):
        if(isinstance(obj,dict)):
            current_handle={}
        if(isinstance(obj,list)):
            current_handle=[]
    
    if(isinstance(obj,dict)):
        d={}
        for key in obj.keys():
            d[key]=pyson_deep_copy(obj[key],obj_id,root_id,output_obj,output_root)
        return d
    if(isinstance(obj,list)):
        l=[]
        for i in range(0,len(obj)):
            l.append(pyson_deep_copy(obj[i],obj_id,root_id,output_obj,output_root))
        return l
    
    raise RuntimeError("Impossible condition")
    
def default_warp_function(checker):
    #the list warper
    if(isinstance(checker,list)):
        new_checker=c.EnumChecker(checker)
        return new_checker
    #the dict warper
    if(isinstance(checker,dict)):
        new_checker=c.DictChecker(checker)
        return new_checker
    #the string warper
    if(isinstance(checker,str)):
        if(checker=="int"):
            return c.IntChecker()
        if(checker=="float"):
            return c.FloatChecker()
        if(checker=="bool"):
            return c.BoolChecker()
        if(checker=="string"):
            return c.StringChecker()
        if(checker=="self"):
            return c.SelfChecker()
        if(checker=="none"):
            return c.NoneChecker()
    return checker


def intable(value):
    try:
        int(value)
        return True
    except:
        return False


class DotDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        self.__dict__ = self

class Transformer(object):
    def __init__(self,reg):
        self.reg=reg
        self.warp_function=default_warp_function
    
    def _get_object(self,object_name,scope,output_root):
        if(scope=="name"):
            return self.reg.get_object(object_name)
        if(scope=="import"):
            pack_obj=self.reg.load_package_object(object_name)
            if(pack_obj is None):
                return None
            return (pack_obj,None)
        if(scope=="self"):
            object_name=object_name.split('.')
            current_node=output_root
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
    
    def make_filting(self, node, checker, filter_list=None):
        pattern=r'^[A-Za-z_]+([A-Za-z0-9_])*$'
        for element in filter_list:
            if(re.match(pattern,element) is None):
                raise RuntimeError("The "+element+" is not a key")
        
        node_dict=node.value
        if(not isinstance(node_dict,dict)):
            raise RuntimeError("The filter operation is just for the dict")

        key_list=list(node_dict.keys())
        for key in key_list:
            if(key not in filter_list):
                del node_dict[key]
        
        if(checker is None):
            return node,checker
        
        checker=self.warp_function(checker)
        new_checker=checker.generate_filter_checker(filter_list)
        return node,new_checker
    
    #current_list is the current_untransformed note,output is the filling store
    #output_root is the root of the ctx  
    #row_dict is also should be used for checker node
    #the checker is also important
    #transform list is totally the mass
    def _transform_list(self,node,node_root,output,output_root,location="",checker=None,instance=True):
        checker=self.warp_function(checker)
        current_list=node.value
        if(checker is not None):
            checker._check(node,node_root,location)
        for i in range(0,len(current_list)):
            #get the obj_checker
            obj_checker=None
            if(checker is not None):
                obj_checker=checker.get_element_checker(i,node)
            #set current location
            current_location=location
            current_location=current_location+"."+str(i)
            #checker the type
            if(isinstance(current_list[i].value,(int,float,bool,str,type(None)))):
                obj_checker=self.warp_function(obj_checker)
                if(obj_checker is not None):
                    obj_checker._check(current_list[i],node_root,current_location)
                if(instance):
                    output.append(current_list[i].value)
                continue
            if(isinstance(current_list[i].value,pyson.regist_object.RegistObject) and current_list[i].value.scope!="self"):
                if(instance):
                    store=[]
                    self._transform_object(current_list[i],node_root,store,output_root,current_location,obj_checker,instance)
                    output.append(store[0])
                else:
                    self._transform_object(current_list[i],node_root,[output[i]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,pyson.regist_object.RegistObject) and current_list[i].value.scope=="self"):
                if(instance):
                    store=[]
                    self._transform_self(current_list[i],node_root,store,output_root,current_location,obj_checker,instance)
                    output.append(store[0])
                else:
                    self._transform_self(current_list[i],node_root,[output[i]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,list)):
                if(instance):
                    store=[]
                    output.append(store)
                    self._transform_list(current_list[i],node_root,store,output_root,current_location,obj_checker,instance)
                else:
                    self._transform_list(current_list[i],node_root,[output[i]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_list[i].value,dict)):
                if(instance):
                    store=DotDict()
                    output.append(store)
                    self._transform_dict(current_list[i],node_root,store,output_root,current_location,obj_checker,instance)
                else:
                    self._transform_dict(current_list[i],node_root,output[i],output_root,current_location,obj_checker,instance)
                continue

    def _transform_dict(self,node,node_root,output,output_root,location="",checker=None,instance=True):
        checker=self.warp_function(checker)
        current_dict=node.value
        if(checker is not None):
            checker._check(node,node_root,location)
        for key,value in current_dict.items():
            #set error location
            current_location=location
            current_location=current_location+"."+str(key)
            #get the checker
            obj_checker=None
            if(checker is not None):
                obj_checker=checker.get_element_checker(key,node)
            #check the type
            if(isinstance(current_dict[key].value,(int,float,bool,str,type(None)))):
                obj_checker=self.warp_function(obj_checker)
                if(obj_checker is not None):
                    obj_checker._check(current_dict[key],node_root,current_location)
                if(instance):
                    output[key]=value.value
                continue
            if(isinstance(current_dict[key].value,pyson.regist_object.RegistObject) and current_dict[key].value.scope!="self"):
                if(instance):
                    store=[]
                    self._transform_object(current_dict[key],node_root,store,output_root,current_location,obj_checker,instance)
                    output[key]=store[0]
                else:
                    self._transform_object(current_dict[key],node_root,[output[key]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,pyson.regist_object.RegistObject) and current_dict[key].value.scope=="self"):
                if(instance):
                    store=[]
                    self._transform_self(current_dict[key],node_root,store,output_root,current_location,obj_checker,instance)
                    output[key]=store[0]
                else:
                    self._transform_self(current_dict[key],node_root,[output[key]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,list)):
                if(instance):
                    store=[]
                    output[key]=store
                    self._transform_list(current_dict[key],node_root,store,output_root,current_location,obj_checker,instance)
                else:
                    self._transform_list(current_dict[key],node_root,[output[key]],output_root,current_location,obj_checker,instance)
                continue
            if(isinstance(current_dict[key].value,dict)):
                if(instance):
                    store=DotDict()
                    output[key]=store
                    self._transform_dict(current_dict[key],node_root,store,output_root,current_location,obj_checker,instance)
                else:
                    self._transform_dict(current_dict[key],node_root,output[key],output_root,current_location,obj_checker,instance)
                continue


    def _transform_object(self,node,node_root,output,output_root,location="",checker=None,instance=True):
        checker=self.warp_function(checker)
        regist_object=node.value
        if(checker is not None):
            checker._check(node,node_root,location)
        if(instance):
            obj_class=self._get_object(regist_object.object_name,regist_object.scope,output_root)
            if(obj_class is None):
                print_obj_name=regist_object.object_name
                if(regist_object.scope=="name"):
                    print_obj_name="@"+print_obj_name
                raise TransformWrongError("The object '"+print_obj_name+"' can not be found",
            location,node.line,node.column)
            if(regist_object.params is None):
                output.append(obj_class[0])
                return
            #if the regist_object.params is not none then check the obj_class[1]
            if(isinstance(regist_object.params.value,dict)):
                params={}
                self._transform_dict(regist_object.params,node_root,params,output_root,location+"#params",obj_class[1],instance)
                #if the params is wrong throw the exception
                # params=pyson_deep_copy(params,id(params),id(output_root))
                obj=None
                try:
                    obj=obj_class[0](**params)
                    output.append(obj)
                except Exception as e:
                    raise TransformWrongError("The params for object '"+regist_object.object_name+"' is wrong",
                    location,node.line,node.column,obj_class[0].__name__+": "+str(e))
                return
            if(isinstance(regist_object.params.value,list)):
                if(obj_class[1] is None):
                    params_list=[]
                    self._transform_list(regist_object.params,node_root,params_list,output_root,location+"#params",None)
                    # params_list=pyson_deep_copy(params_list,id(params_list),id(output_root))                 
                    try:
                        obj=obj_class[0](*params_list)
                        output.append(obj)
                    except Exception as e:
                        raise TransformWrongError("The params for object '"+regist_object.object_name+"' is wrong",
                        location,node.line,node.column,obj_class[0].__name__+": "+str(e))
                    return
                else:
                    #special case for the params_list ,first it should be transformed in to dict
                    params_list=regist_object.params.value
                    dict_checker=obj_class[1]
                    dict_checker=self.warp_function(dict_checker)
                    #get the function params list
                    func=obj_class[0]
                    function_params_list=None
                    if(not isfunction(func)):
                        if(isinstance(func,type)):
                            func=func.__init__
                            function_params_list=list(func.__code__.co_varnames)[1:]
                        else:
                            raise TransformWrongError("The object is not callable",location,node.line,node.column)
                    else:
                        function_params_list=list(func.__code__.co_varnames)
                    new_dict=dict_checker.get_params_dict(params_list,function_params_list)
                    params_node=pyson.regist_object.Content(dict,new_dict,node.element_number,node.line,node.column)
                    params={}
                    self._transform_dict(params_node,node_root,params,output_root,location+"#params",dict_checker)
                    # params=pyson_deep_copy(params,id(params),id(output_root))
                    try:
                        obj=obj_class[0](**params)
                        output.append(obj)
                    except Exception as e:
                        raise TransformWrongError("The params for object '"+regist_object.object_name+"' is wrong",
                        location,node.line,node.column,obj_class[0].__name__+": "+str(e))
                    return



    def _transform_self_check(self,node,node_root,output,output_root,location="",checker=None):
        checker=self.warp_function(checker)
        obj=node.value
        if(location=="self"):
            if(checker is not None):
                checker._check(node,node_root,location)
            return 
        if(isinstance(obj,(int,float,bool,str,type(None)))):
            if(checker is not None):
                checker._check(node,node_root,location)
            return
        if(isinstance(obj,pyson.regist_object.RegistObject) and obj.scope!="self"):
            self._transform_object(node,node_root,[output],output_root,location,checker,False)
            return
        if(isinstance(obj,list)):
            self._transform_list(node,node_root,output,output_root,location,checker,False)
            return
        if(isinstance(obj,dict)):
            self._transform_dict(node,node_root,output,output_root,location,checker,False)
            return
        print(obj)
        print(location)
        raise RuntimeError("No possible condition")


    def _index_item(self,node,node_root,output_root,location=""):
        regist_object=node.value
        if(regist_object.params is not None):
            raise TransformWrongError("The self object can not be called",location,node.line,node.column)
        index_string=regist_object.object_name
        if(index_string==""):
            return output_root,node_root,"self"
        indexs=index_string.split(".")
        current_indexing=output_root
        for index in indexs:
            if(intable(index)):
                if(isinstance(current_indexing,list)):
                    if(int(index)<0 or int(index)>=len(current_indexing)):
                        return None
                    current_indexing=current_indexing[int(index)]
                else:
                    return None
            else:
                if(isinstance(current_indexing,dict)):
                    if(index not in current_indexing.keys()):
                        return None
                    current_indexing=current_indexing[index]
                else:
                    return None
        transformed_data=current_indexing
        #current indexing is the data
        #then find the index for node_root
        current_indexing=node_root
        for index in indexs:
            if(intable(index)):
                current_indexing=current_indexing.value[int(index)]
            else:
                current_indexing=current_indexing.value[index]
        raw_data=current_indexing
        if(isinstance(raw_data.value,pyson.regist_object.RegistObject) and raw_data.value.scope=="self"):
            return self._index_item(raw_data,node_root,output_root,"self."+index_string)
        else:
            return transformed_data,raw_data,"self."+index_string
  
  
    def _transform_self(self,node,node_root,output,output_root,location="",checker=None,instance=True):
        regist_object=node.value
        result=self._index_item(node,node_root,output_root)
        if(result is None):
            raise TransformWrongError("Can not find the self."+regist_object.object_name,location,node.line,node.column)
        transformed_data,raw_data,prev_location=result
        #the child could not reference parent
        if(prev_location!="self" and location.startswith(prev_location)):
            raise TransformWrongError("The child could not reference parent "+prev_location,location,node.line,node.column)
        error_accure=False
        reason=None
        try:
            self._transform_self_check(raw_data,node_root,transformed_data,output_root,prev_location,checker)
        except Exception as e:
            error_accure=True
            reason=str(e)
            raise e
        if(error_accure):
            raise TransformWrongError("The 'self."+regist_object.object_name+"' is wrong",
                        location,node.line,node.column,reason)
        if(isinstance):
            if(prev_location!="self"):
                transformed_data=pyson_deep_copy(transformed_data,id(transformed_data),id(output_root))
            output.append(transformed_data)

    def transfrom(self,node,checker=None,dict_filter=[]):
        if(isinstance(node.value,dict)):
            output_root=DotDict()
            output=output_root
            self._transform_dict(node,node,output,output_root,"self",checker)
            return output_root
        if(isinstance(node.value,list)):
            output_root=[]
            output=output_root
            self._transform_list(node,node,output,output_root,"self",checker)
            return output_root
        else:
            return None

            

reg=regist.reg
trans=Transformer(reg)

def set_checker_warper(checker_warp_function):
    trans.warp_function=checker_warp_function


def from_file(file_name,checker_name=None,filter_list=None):
    checker=None
    if(checker_name is not None):
        checker=reg.get_checker(checker_name)
        if(checker is None):
            raise RuntimeError("The "+str(checker_name)+" can not be found")
    node=FileStream(file_name,encoding='utf-8')
    lexer=pyson.pysonLexer.pysonLexer(node)
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
    node=listener.return_value

    if(filter_list is not None):
        node,checker=trans.make_filting(node,checker,filter_list)
    try:
        result=trans.transfrom(node,checker)
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
    node=InputStream(pyson_string)
    lexer=pyson.pysonLexer.pysonLexer(node)
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
    node=listener.return_value

    if(filter_list is not None):
        node,checker=trans.make_filting(node,checker,filter_list)
    try:
        result=trans.transfrom(node,checker)
    except (TransformWrongError,CheckWrongError) as e:
        error_accure=True
        error_msg=str(e)
        error_type=e.__class__
    if(error_accure):
        e=error_type()
        e.set_msg(error_msg)
        raise e
    return result

