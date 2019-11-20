#-*-coding:utf-8 -*-
import re
import pyson.pyson.regist_object as regist_object
from pyson.error import CheckWrongError

from inspect import isfunction



def intable(content):
    try:
        int(content)
        return True
    except:
        return False

def get_type_name(node):
    type_name=str(type(node))
    type_name=type_name.split()[1][1:-2]
    return type_name


class Empty(object):
    def __init__(self):
        pass

    def __str__(self):
        return "'@Empty'"
    
    def __repr__(self):
        return self.__str__()

empty=Empty()

class PysonObjectName(object):
    def __init__(self,object_name):
        self.object_name=object_name
    
    def __str__(self):
        output="'@PysonObjectName:"+self.object_name+"'"
        return output
    
    def __repr__(self):
        return self.__str__()        

class Checker(object):
    def __init__(self):
        self.default=Empty()
        self.location=""
        self.line=0
        self.column=0
        

    def _check_before(self,node,node_root,location):
        self.line=node.line
        self.column=node.column
        self.location=location
        self.check_before(node,node_root)


    def _check_after(self,node,output_root):
        self.check_after(node,output_root)

    def check_before(self,node,node_root):
        pass

    def check_after(self,node,output_root):
        pass
    
    def report_error(self,msg):
        raise CheckWrongError(msg,self.location,self.line,self.column)

    def tips(self):
        return []

    def get_default(self):
        return self.default
    
    def set_location(self,location):
        self.location=location
    
    def __str__(self):
        output=""
        output+="{ "
        output+="'type': "+str(self.__class__.__name__)+", "
        for name,value in vars(self).items(): 
            if(name in ["location","line","column"]):
                continue
            output+="'"+str(name)+"': "+str(value)+", "
        output=output[:-2]
        output+="}"
        return output
    
    def __repr__(self):
        return self.__str__()
    
    

#关于None的问题，例如定义 min_value 首先min_value是optional，然后allow_none应该是False
# 如果定义allow_none为True，那么则允许输入为None。如果default_value 为none则需要设定defualt_value 为 NoneType

class IntChecker(Checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        super(IntChecker,self).__init__()
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        value=node.value
        if(isinstance(value,regist_object.RegistObject)):
            self.report_error("The object call is not allowed, just accept the 'int' type value")

    def check_after(self,node,output_root):
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,int)):
            self.report_error("Input type 'int' is expected but got '"+get_type_name(node)+"'")
        if(self.min_value is not None):
            if(node<self.min_value):
                self.report_error("The input value "+str(node)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(node>self.max_value):
                self.report_error("The input value "+str(node)+" is bigger than the max_value "+str(self.min_value))
    
    def tips(self):
        return []

class FloatChecker(Checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        super(FloatChecker,self).__init__()
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        value=node.value
        if(isinstance(value,regist_object.RegistObject)):
            self.report_error("The object call is not allowed, just accept the 'float' type value")
    
    def check_after(self,output,output_root):
        if(output is None and self.allow_none):
            return
        if(output is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(output,(int,float))):
            self.report_error("Input type float is expected but got "+get_type_name(output))
        if(self.min_value is not None):
            if(output<self.min_value):
                self.report_error("The input value "+str(output)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(output>self.max_value):
                self.report_error("The input value "+str(output)+" is bigger than the max_value "+str(self.min_value))

class StringChecker(Checker):
    def __init__(self,pattern=None,default=empty,allow_none=False):
        super(StringChecker,self).__init__()
        self.pattern=pattern
        self.default=default
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        value=node.value
        if(isinstance(value,regist_object.RegistObject)):
            self.report_error("The object call is not allowed, just accept the 'str' type value")

    def check_after(self,output,output_root):
        if(output is None and self.allow_none):
            return
        if(output is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(output,str)):
            self.report_error("Input type str is expected but got "+get_type_name(output))
        if(self.pattern is not None and re.match(self.pattern,output) is None):
            self.report_error("The input string should match the regular expression "+self.pattern)

class BoolChecker(Checker):
    def __init__(self,default=empty,allow_none=False):
        super(BoolChecker,self).__init__()
        self.default=default
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        value=node.value
        if(isinstance(value,regist_object.RegistObject)):
            self.report_error("The object call is not allowed, just accept the 'bool' type value")
    
    def check_after(self,output,output_root):
        if(output is None and self.allow_none):
            return
        if(output is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(output,bool)):
            self.report_error("Input type 'bool' is expected but got '"+get_type_name(output)+"'")
    
class NoneChecker(Checker):
    def __init__(self):
        super(NoneChecker,self).__init__()
        pass

    def check_before(self,node,node_root):
        value=node.value
        if(isinstance(value,regist_object.RegistObject)):
            self.report_error("The object call is not allowed, just accept the 'None' type value")

    def check_after(self,output,output_root):
        if(output is not None):
            self.report_error("The input should be None")

class SelfChecker(Checker):
    def __init__(self,allow_none=False):
        super(SelfChecker,self).__init__()
        self.allow_none=allow_none

    def check_before(self,node,node_root):
        node=node.value
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(isinstance(node,regist_object.RegistObject)):
            if(node.object_name!="self"):
                self.report_error("The input should be self")
        else:
            self.report_error("The input should be self")

class ObjectChecker(Checker):
    def __init__(self,prefix=None,instance=True,allow_none=False):
        super(ObjectChecker,self).__init__()
        self.prefix=prefix
        self.instance=instance
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        node=node.value
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,regist_object.RegistObject)):
            self.report_error("Input type 'object' is expected but got '"+get_type_name(node)+"'")
        
        if(node.scope!="name"):
            self.report_error("Object name must begin with @")
        #match the pattern,change the match the pattern
        if(self.prefix is not None):
            obj_name=node.object_name
            if(obj_name==self.prefix):
                return
            if(obj_name.startswith(self.prefix+".")):
                return
            self.report_error("The input "+str(object)+" should match the regular expression "+self.prefix)

    def get_default(self):
        if(self.instance):
            return None
        return self.default


#dict need to satisfy the following condition
# 1 The optional key #solution add the optional setting
# 2 The no constrain checker #solution add a no constrain checker for the object or set None
# 3 The unlimit key #solution add a unlimit key option,default is closed
class BaseDictChecker(Checker):
    def __init__(self,checker_dict=None,optional=[],unlimit=False,allow_none=False):
        super(BaseDictChecker,self).__init__()
        if(checker_dict is None):
            self.checker_dict={}
        else:
            self.checker_dict=checker_dict
        self.optional=optional
        self.unlimit=unlimit
        self.allow_none=allow_none

    def check_before(self,node,node_root):
        element_number=node.element_number
        node=node.value
        if(node is None and self.allow_none):
            return True
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,dict)):
            self.report_error("Input type 'dict' is expected but got '"+get_type_name(node)+"'")
        #the node is a ordered dict
        scheme_keys=list(self.checker_dict.keys())
        node_dict_keys=list(node.keys())
        for i in range(0,len(node_dict_keys)):
            current_key=node_dict_keys[i]
            if(current_key not in scheme_keys and self.unlimit):
                continue
            if(current_key not in scheme_keys):
                self.report_error("Key "+str(current_key)+" not found")
            scheme_keys.remove(current_key)
        #if the key not appear in the node
        #it may have the default value or in the optional dict
        for i in range(0,len(scheme_keys)):
            current_key=scheme_keys[i]
            if(current_key in self.optional):
                continue
            item_checker=self.checker_dict[current_key]
            if(item_checker is None):
                self.report_error("Key "+str(current_key)+" is required")
            default_value=item_checker.get_default()
            if(not isinstance(default_value,Empty)):
                node[current_key]=regist_object.Content(type(default_value),default_value,element_number,self.line,self.column)
                continue
            self.report_error("Key "+str(current_key)+" is required")
    
    def _sort_params_key(self,func):
        sort_list=None
        if(not isfunction(func)):
            if(isinstance(func,type)):
                func=func.__init__
                sort_list=list(func.__code__.co_varnames)[1:]
            else:
                raise RuntimeError("The object is not callable, the checker should not been registered")
        else:
            sort_list=list(func.__code__.co_varnames)
        for value in list(self.checker_dict.keys()):
            if(value not in sort_list):
                raise RuntimeError("The key "+str(value)+" dones't appear in params list")
        dict_list=list(self.checker_dict.keys())
        for opt in self.optional:
            if(opt not in dict_list):
                raise RuntimeError("The "+str(opt)+" doesn't appear in dict key")
            

class DictChecker(BaseDictChecker):
    def __init__(self,checker_dict=None,optional=[],unlimit=False,allow_none=False):
        super(DictChecker,self).__init__(checker_dict,optional,unlimit,allow_none)
    
    def add_checker(self,key_name,checker,optional=False):
        if(key_name in self.checker_dict.keys()):
            return
        if(not isinstance(checker,Checker)):
            raise RuntimeError("The checker must be the instace of Checker")
        self.checker_dict[key_name]=checker
        if(optional):
            self.optional.append(key_name)


class ParamsChecker(BaseDictChecker):
    def __init__(self,checker_list=[],optional=[]):
        self.checker_list=checker_list
        self.optional_index_store=[]
        super(ParamsChecker,self).__init__({},optional,False,False)
    
    def _sort_params_key(self,func):
        sort_list=None
        if(not isfunction(func)):
            if(isinstance(func,type)):
                func=func.__init__
                sort_list=list(func.__code__.co_varnames)[1:]
            else:
                raise RuntimeError("The object is not callable, the checker should not been registered")
        else:
            sort_list=list(func.__code__.co_varnames)

        if(len(sort_list)<len(self.checker_list)):
            raise RuntimeError("The number of checkers is  more than the number of params")

        for i in range(0,len(self.checker_list)):
            param=sort_list[i]
            self.checker_dict[param]=self.checker_list[i]

        for index in self.optional_index_store:
            self.optional.append(sort_list[index])

        new_dict_list=list(self.checker_dict.keys())
        for opt in self.optional:
            if(opt not in new_dict_list):
                raise RuntimeError("The "+str(opt)+" doesn't appear in dict key")

    def add_checker(self,checker,optional=False):
        self.checker_list.append(checker)
        if(optional):
            self.optional_index_store.append(len(self.checker_list)-1)
    


#the list checker for check list
class ListChecker(Checker):
    def __init__(self,element_checker=None,max_numbers=-1,allow_none=False):
        super(ListChecker,self).__init__()
        self.element_checker=element_checker
        self.max_numbers=max_numbers
        self.allow_none=allow_none
    
    def check_before(self,node,node_root):
        node=node.value
        if(node is None and self.allow_none):
            return
        if(node is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(node,list)):
            self.report_error("Input type 'list' is expected but got '"+get_type_name(node)+"'")
        for i in range(0,len(node)):
            element=node[i]
            if(not self._check_single_before(element,node_root)):
                print(self.element_checker)
                self.report_error("The input type doesn't satisify the list type requirement "+str(element.value))
    
    def check_after(self,output,output_root):
        for i in range(0,len(output)):
            element=output[i]
            if(not self._check_single_after(element,output_root)):
                self.report_error("The input type doesn't satisify the list type requirement")

    
    def _check_single_before(self,element,output_root):
        if(self.element_checker is None):
            return True
        try:
            self.element_checker._check_before(element,output_root,self.location)
            return True
        except:
            return False
    
    def _check_single_after(self,element,output_root):
        if(self.element_checker is None):
            return True
        try:
            self.element_checker._check_after(element,output_root)
            return True
        except:
            return False
        

    def get_default(self):
        return None


#enum type
class EnumChecker(Checker):
    def __init__(self,enums=[],instance=True):
        super(EnumChecker,self).__init__()
        self.enums=enums
        self.instance=instance
        for i in range(0,len(self.enums)):
            item=enums[i]
            if(item is None):
                continue
            if(isinstance(item,(float,int,str,bool,regist_object.RegistObjectName))):
                continue
            raise RuntimeError("Unsupport value in enumeration")
    
    def _check_regist_object(self,node):
        for i in range(0,self.enums):
            item=self.enums[i]
            if(isinstance(regist_object.RegistObjectName)):
                if(item.pyson_name==node.pyson_name and item.scope==node.scope):
                    return True
        return False
            
    
    def check_before(self,node,node_root):
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
        if(isinstance(node,regist_object.RegistObject)):
            if(self._check_regist_object(node)):
                return
            else:
                self.report_error("The value "+str(node.scope)+"#"+str(node.pyson_name)+" not in the enumeration")


