#-*-coding:utf-8 -*-
import re
import pyson.pyson.pyson_object as pyson_object
from collections import OrderedDict
from pyson.error import CheckWrongError

class empty_type(object):
    def __init__(self):
        pass

empty=empty_type()

def intable(content):
    try:
        int(content)
        return True
    except:
        return False

def find_in_raw(raw_dict,object_name,element_number):
    def _find_in_raw(raw_dict,object_name):
        current_ctx=raw_dict
        keys=object_name.split(".")
        for key in keys:
            if(intable(key)):
                if(isinstance(current_ctx.value,list)):
                    if(int(key)>=len(current_ctx.value)):
                        return None
                    current_ctx=current_ctx.value[int(key)]
                    continue
                return None
            else:
                if(isinstance(current_ctx.value,dict)):
                    if(key in current_ctx.value.keys()):
                        current_ctx=current_ctx.value[key]
                        continue
                    else:
                        return None
                return None
        return current_ctx
    search_obj_type=False
    params=None
    while(True):
        current_ctx=_find_in_raw(raw_dict,object_name)
        if(current_ctx is None):
            return None
        if(not isinstance(current_ctx.value,pyson_object.pyson_object)):
            return None
        obj=current_ctx.value
        if(not search_obj_type):
            if(obj.scope=="self" and obj.params is None):
                if(current_ctx.element_number>=element_number):
                    return None
                element_number=obj.element_number
                current_ctx=_find_in_raw(raw_dict,obj.object_name)
            if(obj.scope!="self"):
                if(current_ctx.element_number>=element_number):
                    return None
                return current_ctx
            if(obj.scope=="self" and obj.params is not None):
                search_obj_type=True
                params=obj.params
                element_number=obj.element_number
                current_ctx=_find_in_raw(raw_dict,obj.object_name)
        else:
            if(obj.params is not None):
                return None
            if(obj.scope=="self"):
                element_number=obj.element_number
                current_ctx=_find_in_raw(raw_dict,obj.object_name)
            if(obj.scope!="self"):
                pys_obj=pyson_object.pyson_object(obj.object_name,obj.scope,params)
                cont=pyson_object.content(current_ctx.type,pys_obj,element_number,current_ctx.line,current_ctx.column)
                return cont
            

class checker(object):
    def __init__(self):
        self.default=None
        self.location=""
        self.line=0
        self.column=0
        

    def _check_before(self,current_node,raw_dict,location):
        self.line=current_node.line
        self.column=current_node.column
        self.location=location
        self.check_before(current_node,raw_dict)


    def _check_after(self,current_node,ctx):
        self.check_after(current_node,ctx)

    def check_before(self,current_node,raw_dict):
        pass

    def check_after(self,current_node,ctx):
        pass
    
    def report_error(self,msg):
        raise CheckWrongError(msg,self.location,self.line,self.column)

    def tips(self):
        return []

    def get_default(self):
        return self.default
    
    def set_location(self,location):
        self.location=location

#关于None的问题，例如定义 min_value 首先min_value是optional，然后allow_none应该是False
# 如果定义allow_none为True，那么则允许输入为None。如果default_value 为none则需要设定defualt_value 为 NoneType

class int_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        super(int_checker,self).__init__()
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none

    def check_after(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,int)):
            self.report_error("Input type int is expected but got "+str(type(node)))
        if(self.min_value is not None):
            if(node<self.min_value):
                self.report_error("The input value "+str(node)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(node>self.max_value):
                self.report_error("The input value "+str(node)+" is bigger than the max_value "+str(self.min_value))
    
    def tips(self):
        return []

class float_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        super(float_checker,self).__init__()
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
    
    def check_after(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,(int,float))):
            self.report_error("Input type float is expected but got "+str(type(node)))
        if(self.min_value is not None):
            if(node<self.min_value):
                self.report_error("The input value "+str(node)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(node>self.max_value):
                self.report_error("The input value "+str(node)+" is bigger than the max_value "+str(self.min_value))
    
    def tips(self):
        return []

class string_checker(checker):
    def __init__(self,pattern=None,default=empty,allow_none=False):
        super(string_checker,self).__init__()
        self.pattern=pattern
        self.default=default
        self.allow_none=allow_none

    def check_after(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,str)):
            self.report_error("Input type str is expected but got "+str(type(node)))
        if(self.pattern is not None and re.match(self.pattern,node) is None):
            self.report_error("The input string should match the regular expression "+self.pattern)

class bool_checker(checker):
    def __init__(self,default=empty,allow_none=False):
        super(bool_checker,self).__init__()
        self.default=default
        self.allow_none=allow_none
    
    def check_after(self,node,ctx):
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,bool)):
            self.report_error("Input type bool is expected but got "+str(type(node)))
    
class none_checker(checker):
    def __init__(self):
        super(none_checker,self).__init__()
        pass

    def check_after(self,node,ctx):
        if(node is not None):
            self.report_error("The input should be None")

class self_checker(checker):
    def __init__(self,allow_none=False):
        super(self_checker,self).__init__()
        self.allow_none=allow_none

    def check_before(self,node,raw_dict):
        node=node.value
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(isinstance(node,pyson_object.pyson_object)):
            if(node.object_name!="self"):
                self.report_error("The input should be self")
        else:
            self.report_error("The input should be self")

class object_checker(checker):
    def __init__(self,pattern=None,instance=True,allow_none=False):
        super(object_checker,self).__init__()
        self.pattern=pattern
        self.instance=instance
        self.allow_none=allow_none
    
    def check_before(self,node,raw_dict):
        node=node.value
        element_number=node.element_number
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,pyson_object.pyson_object)):
            self.report_error("Input type object is expected but got "+str(type(node)))
        
        #match the pattern 
        if(self.pattern is not None):
            object=node.scope+"@"+node.object_name
            if(re.match(self.pattern,object) is not None):
                self.report_error("The input "+str(object)+" should match the regular expression "+self.pattern)
        
        #check if the element in the current dict
        if(node.scope=="self"):
            prev_node=find_in_raw(raw_dict,node.object_name,element_number)
            if(prev_node is None):
                self.report_error("The "+node.object_name+" could not be found")
            if(not self.instance):
                if(node.params is not None):
                    self.report_error("The object is an instance type, set the instance be True")
                if(prev_node.params is not None):
                    self.report_error("The object is an instance type, set the instance be True")
                return
            else:
                if(node.params is not None and prev_node.params is not None):
                    self.report_error("The multiple calls")
                if(node.params is None and prev_node.params is None):
                    self.report_error("The object should not be instanced, set the instance be False")
                return

    def get_default(self):
        if(self.instance):
            return None
        return self.default


#dict need to satisfy the following condition
# 1 The optional key #solution add the optional setting
# 2 The no constrain checker #solution add a no constrain checker for the object or set None
# 3 The unlimit key #solution add a unlimit key option,default is closed
class dict_checker(checker):
    def __init__(self,scheme=OrderedDict(),optional=[],unlimit=False,allow_none=False):
        super(dict_checker,self).__init__()
        self.scheme=scheme
        self.optional=optional
        self.unlimit=unlimit
        self.allow_none=allow_none

    
    def check_before(self,node,ctx):
        element_number=node.element_number
        node=node.value
        if(node is None and self.allow_none):
            return True
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,dict)):
            self.report_error("Input type dict is expected but got "+str(type(node)))
        #the node is a ordered dict
        scheme_keys=list(self.scheme.keys())
        node_dict_keys=list(node.keys())
        for i in range(0,len(node_dict_keys)):
            current_key=node_dict_keys[i]
            if(current_key not in scheme_keys and self.unlimit):
                continue
            if(current_key not in scheme_keys):
                self.report_error("Key "+str(current_key)+" not found in dict define")
            item_checker=self.scheme[current_key]
            del scheme_keys[current_key]
        #if the key not appear in the node
        #it may have the default value or in the optional dict
        for i in range(0,len(scheme_keys)):
            current_key=scheme_keys[i]
            if(current_key in self.optional):
                continue
            item_checker=self.scheme[current_key]
            if(item_checker is None):
                self.report_error("Key "+str(current_key)+" is required in dict define")
            default_value=item_checker.get_default()
            if(not isinstance(default_value,empty_type)):
                node[current_key]=pyson_object.content(type(default_value),default_value,element_number,self.line,self.column)
                continue
            self.report_error("Key "+str(current_key)+" is required in dict define")


#the list checker for check list
class list_checker(checker):
    def __init__(self,element_checker=None,max_numbers=-1,allow_none=False):
        super(list_checker,self).__init__()
        self.element_checker=element_checker
        self.max_numbers=max_numbers
        self.allow_none=allow_none
    
    def check_before(self,node,raw_dict):
        node=node.value
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,list)):
            self.report_error("Input type list is expected but got "+str(type(node)))
        for i in range(0,len(node)):
            element=node[i]
            if(not self._check_single_before(element,raw_dict)):
                self.report_error("The input type doesn't satisify the list type requirement"+str(type(node)))
    
    def check_after(self,node,ctx):
        for i in range(0,len(node)):
            element=node[i]
            if(not self._check_single_after(element,ctx)):
                self.report_error("The input type doesn't satisify the list type requirement"+str(type(node)))

    
    def _check_single_before(self,element,raw_dict):
        if(self.element_checker is None):
            return True
        try:
            element.check_before(element,ctx)
            return True
        except:
            return False
    
    def _check_single_after(self,element,raw_dict):
        if(self.element_checker is None):
            return True
        try:
            element.check_after(element,ctx)
            return True
        except:
            return False
        

    def get_default(self):
        return None


#enum type
class enum_checker(checker):
    def __init__(self,enums=[],instance=True):
        super(enum_checker,self).__init__()
        self.enums=enums
        self.instance=instance
        for i in range(0,len(self.enums)):
            item=enums[i]
            if(item is None):
                continue
            if(isinstance(item,(float,int,str,bool,pyson_object.pyson_name))):
                continue
            raise RuntimeError("Unsupport value in enumeration")
    
    def _check_pyson_object(self,node):
        for i in range(0,self.enums):
            item=self.enums[i]
            if(isinstance(pyson_object.pyson_name)):
                if(item.pyson_name==node.pyson_name and item.scope==node.scope):
                    return True
        return False
            
    
    def check_before(self,node,raw_dict):
        node=node.value
        if(node is None):
            if(node in self.enums):
                return
            else:
                self.report_error("The value None not in the enumeration")
        if(isinstance(node,(float,int,str,bool))):
            if(node in self.enums):
                return
            else:
                self.report_error("The value "+str(node)+" not in the enumeration")
        if(isinstance(node,pyson_object.pyson_object)):
            if(self._check_pyson_object(node)):
                return
            else:
                self.report_error("The value "+str(node.scope)+"#"+str(node.pyson_name)+" not in the enumeration")


