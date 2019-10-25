#-*-coding:utf-8 -*-
import re
import pyson.pyson.pyson_object as pyson_object
import pyson.regist as regist
from collections import OrderedDict

#pyson checker存在以下几个遗留问题
#problem 2:  the support for the basic type value params
class empty_type(object):
    def __init__(self):
        pass

empty=empty_type()

class CheckWrongError(Exception):
    def __init__(self,msg,location):
        self.msg=msg
        self.location=location
    
    def str(self):
        return_value=self.location+":"+self.msg
        return str(return_value)

def intable(content):
    try:
        int(content)
        return True
    except:
        return False

def check_ctx(ctx,object_name):
    current_ctx=ctx
    keys=object_name.split(".")
    for key in keys:
        if(intable(key)):
            if(isinstance(current_ctx,list)):
                if(int(key)>=len(current_ctx)):
                    return None
                current_ctx=current_ctx[int(key)]
                continue
            return None
        else:
            if(isinstance(current_ctx,dict)):
                if(key in current_ctx.keys()):
                    current_ctx=current_ctx[key]
                    continue
                else:
                    return None
            return None
    if(isinstance(current_ctx,pyson_object.pyson_name)):
        return current_ctx
    else:
        return None

#check the basic type 
#int float str bool object_name
def check_basic_type(node,ctx,check_type):
    if(isinstance(node,check_type)):
        return
    if(isinstance(node,pyson_object.pyson_object)):
        if()
        

class checker(object):
    def __init__(self):
        self.default=None
        self.location=""

    def check(self,node,ctx):
        pass

    def tips(self):
        return []

    def get_default(self):
        return self.default
    
    def set_location(self,location):
        self.location=location

class int_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))

    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,int)):
            raise CheckWrongError("Input type int is expected but got "+str(type(node)),self.location)
        if(self.min_value is not None):
            if(node<self.min_value):
                raise CheckWrongError("The input value "+str(node)+" is smaller than the min_value "+str(self.min_value),self.location)
        if(self.max_value is not None):
            if(node>self.max_value):
                raise CheckWrongError("The input value "+str(node)+" is bigger than the max_value "+str(self.min_value),self.location)
    
    def tips(self):
        return []

class float_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=None,allow_none=False):
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,(int,float))):
            raise CheckWrongError("Input type float is expected but got "+str(type(node)),self.location)
        if(self.min_value is not None):
            if(node<self.min_value):
                raise CheckWrongError("The input value "+str(node)+" is smaller than the min_value "+str(self.min_value),self.location)
        if(self.max_value is not None):
            if(node>self.max_value):
                raise CheckWrongError("The input value "+str(node)+" is bigger than the max_value "+str(self.min_value),self.location)
    
    def tips(self):
        return []

class string_checker(checker):
    def __init__(self,pattern=None,default=None,allow_none=False):
        self.pattern=pattern
        self.default=default
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))

    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,str)):
            raise CheckWrongError("Input type str is expected but got "+str(type(node)),self.location)
        if(self.pattern is not None and re.match(self.pattern,node) is None):
            raise CheckWrongError("The input string should match the regular expression "+self.pattern,self.location)

class bool_checker(checker):
    def __init__(self,default=None,allow_none=False):
        self.default=default
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,bool)):
            raise CheckWrongError("Input type bool is expected but got "+str(type(node)),self.location)

class object_name_checker(checker):
    def __init__(self,pattern=None,default=None,allow_none=False):
        self.pattern=pattern
        self.default=default
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,pyson_object.pyson_object)):
            raise CheckWrongError("Input type object is expected but got "+str(type(node)),self.location)
        #match the pattern 
        if(self.pattern is not None):
            object=node.scope+"#"+node.object_name
            if(re.match(self.pattern,object) is not None):
                raise CheckWrongError("The input "+str(object)+" should match the regular expression "+self.pattern,self.location)


    
class none_checker(checker):
    def __init__(self):
        pass

    def check(self,node,ctx):
        if(node is not None):
            raise CheckWrongError("The input should be None",self.location)

class ctx_checker(checker):
    def __init__(self,allow_none=False):
        self.allow_none=allow_none

    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(isinstance(node,tuple)):
            if(node[0]!="ctx"):
                raise CheckWrongError("The input should be ctx",self.location)
        else:
            raise CheckWrongError("The input should be ctx",self.location)

class object_checker(checker):
    def __init__(self,pattern=None,default=None,instance=True,allow_none=False):
        self.pattern=pattern
        self.default=default
        self.instance=instance
        self.allow_none=allow_none
        if(not isinstance(self.default,empty_type) and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,pyson_object.pyson_object)):
            raise CheckWrongError("Input type object is expected but got "+str(type(node)),self.location)
        #match the pattern 
        if(self.pattern is not None):
            object=node.scope+"@"+node.object_name
            if(re.match(self.pattern,object) is not None):
                raise CheckWrongError("The input "+str(object)+" should match the regular expression "+self.pattern,self.location)
        
        #find the element in reg and ctx
        reg=regist.reg
        object_tuple=reg.get_object(node.object_name,node.scope)
        if(object_tuple is not None):
             #instance check
            if(not self.instance):
                if(node.params is not None):
                   raise CheckWrongError("The object is an instance type, set the instance be True",self.location)
                return
            if(node.params is None):
                raise CheckWrongError("The object should not be instanced, set the instance be False",self.location)
            self._check_params(node.node_params,object_tuple[1],ctx)
        else:
            #check if the element in the current dict
            if(node.scope=="self"):
                prev_node=check_ctx(ctx,node.object_name)
                if(prev_node is None):
                    raise CheckWrongError("The "+node.object_name+" could not be found",self.location)
                if(not self.instance):
                    if(prev_node.params is not None):
                        raise CheckWrongError("The object is an instance type, set the instance be True",self.location)
                    return
                if(node.params is None):
                    raise CheckWrongError("The object should not be instanced, set the instance be False",self.location)
                return
            else:
                raise CheckWrongError("The "+node.object_name+" could not be found",self.location)
    
    def _check_params(self,node_params,scheme,ctx):
        d_checker=dict_checker(scheme)
        d_checker.set_location(self.location)
        if(isinstance(node_params,list)):
            node_params_dict=OrderedDict()
            scheme_keys=list(scheme.keys())
            if(len(scheme_keys)<len(node_params)):
                raise CheckWrongError("The wrong parameter list",self.location)
            for i in range(0,len(node_params)):
                node_params_dict[scheme_keys[i]]=node_params[i]
            d_checker.check(node_params_dict,ctx)
        if(isinstance(node_params,dict)):
            d_checker.check(node_params,ctx)
        raise CheckWrongError("The unexpected error",self.location)

    def get_default(self):
        if(self.instance):
            return None
        return self.default


#dict need to satisfy the following condition
# 1 The optional key #solution add the optional setting
# 2 The no constrain checker #solution add a no constrain checker for the object or set None
# 3 The unlimit key #solution add a unlimit key option,default is closed
class dict_checker(checker):
    def __init__(self,scheme,optional=[],unlimit=False,allow_none=False):
        self.scheme=scheme
        self.optional=optional
        self.unlimit=unlimit
        self.allow_none=allow_none

    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return True
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,dict)):
            raise CheckWrongError("Input type dict is expected but got "+str(type(node)),self.location)
        #the node is a ordered dict
        scheme_keys=list(self.scheme.keys())
        node_dict_keys=list(node.keys())
        for i in range(0,len(node_dict_keys)):
            current_key=node_dict_keys[i]
            if(current_key not in scheme_keys and self.unlimit):
                continue
            if(current_key not in scheme_keys):
                raise CheckWrongError("Key "+str(current_key)+" not found in dict define",self.location+"."+str(current_key))
            item_checker=self.scheme[current_key]
            if(item_checker is None):
                continue
            item_checker.set_location(self.location+"."+current_key)
            item_checker.check(node[current_key],ctx)
            del scheme_keys[current_key]
        #if the key not appear in the node
        #it may have the default value or in the optional dict
        for i in range(0,len(scheme_keys)):
            current_key=scheme_keys[i]
            if(current_key in self.optional):
                continue
            item_checker=self.scheme[current_key]
            if(item_checker is None):
                raise CheckWrongError("Key "+str(current_key)+" is required in dict define",self.location+"."+str(current_key))
            default_value=item_checker.get_default()
            if(not isinstance(default_value,empty_type)):
                node[current_key]=default_value
                continue
            raise CheckWrongError("Key "+str(current_key)+" is required in dict define",self.location+"."+str(current_key))


#the list checker for check list
class list_checker(checker):
    def __init__(self,checkers=[],max_numbers=-1,allow_none=False):
        self.checkers=checkers
        self.max_numbers=max_numbers
        self.allow_none=allow_none
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            raise CheckWrongError("The value should not be None, set the allow_none be True for None value",self.location)
        if(not isinstance(node,list)):
            raise CheckWrongError("Input type list is expected but got "+str(type(node)),self.location)
        for i in range(0,len(node)):
            element=node[i]
            if(not self._check_single(element,ctx,i)):
                raise CheckWrongError("The input type doesn't satisify the list type requirement"+str(type(node)),self.location)
    
    def _check_single(self,element,ctx,index):
        if(len(self.checkers)==0):
            return True
        for checker in self.checkers:
            try:
                checker.set_location(self.location+"["+str(index)+']')
                checker.check(element,ctx)
                return True
            except:
                continue
        return False
        

    def get_default(self):
        return None

#enum type
class enum_checker(checker):
    def __init__(self,enums=[],instance=True):
        self.enums=enums
        self.instance=instance
        for i in range(0,len(self.enums)):
            item=enums[i]
            if(item is None):
                continue
            if(isinstance(item,(float,int,str,bool,pyson_object.pyson_name))):
                continue
            raise RuntimeError("Eorror for enums")
    
    def _check_pyson_object(self,node):
        for i in range(0,self.enums):
            item=self.enums[i]
            if(isinstance(pyson_object.pyson_name)):
                if(item.pyson_name==node.pyson_name and item.scope==node.scope):
                    return True
        return False
            
    
    def check(self,node,ctx):
        if(node is None):
            if(node in self.enums):
                return
            else:
                raise CheckWrongError("The value None not in the enumeration",self.location)
        if(isinstance(node,(float,int,str,bool))):
            if(node in self.enums):
                return
            else:
                raise CheckWrongError("The value "+str(node)+" not in the enumeration",self.location)
        if(isinstance(node,pyson_object.pyson_object)):
            if(self._check_pyson_object(node)):
                obj_checker=object_checker(instance=self.instance)
                obj_checker.set_location(self.location)
                obj_checker.check(node,ctx)
            else:
                raise CheckWrongError("The value "+str(node.scope)+"#"+str(node.pyson_name)+" not in the enumeration",self.location)


