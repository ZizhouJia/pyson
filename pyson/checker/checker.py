#-*-coding:utf-8 -*-
import re
import pyson.pyson.regist_object as regist_object
from pyson.error import CheckWrongError
from pyson.error import ReigistError

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

class ObjectName(object):
    def __init__(self,object_name,instance=True):
        self.object_name=object_name
        self.instance=instance
    
    def __str__(self):
        output="'@ObjectName:"+self.object_name+"'"
        return output
    
    def __repr__(self):
        return self.__str__()        

class Checker(object):
    def __init__(self):
        self.default=Empty()
        self.location=""
        self.line=0
        self.column=0
        

    def _check(self,node,node_root,location):
        self.line=node.line
        self.column=node.column
        self.location=location
        self.check(node,node_root)

    def check(self,node,node_root):
        pass

    def report_error(self,msg):
        raise CheckWrongError(msg,self.location,self.line,self.column)

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
    
    def check(self,node,node_root):
        value=node.value
        if(value is None and self.allow_none):
            return
        if(value is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(value,int)):
            self.report_error("Input type 'int' is expected but got '"+get_type_name(value)+"'")
        if(self.min_value is not None):
            if(value<self.min_value):
                self.report_error("The input value "+str(value)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(value>self.max_value):
                self.report_error("The input value "+str(value)+" is bigger than the max_value "+str(self.min_value))


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

class FloatChecker(Checker):
    def __init__(self,min_value=None,max_value=None,default=empty,allow_none=False):
        super(FloatChecker,self).__init__()
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
    
    def check(self,node,node_root):
        value=node.value
        if(value is None and self.allow_none):
            return
        if(value is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(value,(int,float))):
            self.report_error("Input type float is expected but got "+get_type_name(value))
        if(self.min_value is not None):
            if(value<self.min_value):
                self.report_error("The input value "+str(value)+" is smaller than the min_value "+str(self.min_value))
        if(self.max_value is not None):
            if(value>self.max_value):
                self.report_error("The input value "+str(value)+" is bigger than the max_value "+str(self.min_value))
    
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
    
    def check(self,node,node_root):
        value=node.value
        if(value is None and self.allow_none):
            return
        if(value is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(value,str)):
            self.report_error("Input type str is expected but got "+get_type_name(value))
        if(self.pattern is not None and re.match(self.pattern,value) is None):
            self.report_error("The input string should match the regular expression "+self.pattern)

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
    
    def check(self,node,node_root):
        value=node.value
        if(value is None and self.allow_none):
            return
        if(value is None):
            self.report_error("The value should not be None, set the allow_none be True for None value")
        if(not isinstance(value,bool)):
            self.report_error("Input type 'bool' is expected but got '"+get_type_name(value)+"'")
    
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

    def check(self,node,node_root):
        value=node.value
        if(value is not None):
            self.report_error("The input should be None")

    def check_after(self,output,output_root):
        if(output is not None):
            self.report_error("The input should be None")

class SelfChecker(Checker):
    def __init__(self,allow_none=False):
        super(SelfChecker,self).__init__()
        self.allow_none=allow_none

    def check(self,node,node_root):
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
    
    def check(self,node,node_root):
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
    def __init__(self):
        super(BaseDictChecker,self).__init__()

    def get_element_checker(self,key,node):
        raise NotImplementedError("The function need to be implemented")

    def get_params_dict(self,params_list,function_params_list):
        raise NotImplementedError("The function need to be implemented")

class DictChecker(BaseDictChecker):
    def __init__(self,checker_dict=None,optional=[],unlimit=False,allow_none=False):
        super(DictChecker,self).__init__()
        if(checker_dict is None):
            self.checker_dict={}
        else:
            self.checker_dict=checker_dict
        self.optional=optional
        self.unlimit=unlimit
        self.allow_none=allow_none
    
    def check(self,node,node_root):
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

    
    def add_checker(self,key_name,checker,optional=False):
        if(key_name in self.checker_dict.keys()):
            return
        if(not isinstance(checker,Checker)):
            raise RuntimeError("The checker must be the instace of Checker")
        self.checker_dict[key_name]=checker
        if(optional):
            self.optional.append(key_name)
    
    def generate_filter_checker(self,filter_list=None):
        if(filter_list is None):
            return self
        new_dict={}
        for key in filter_list:
            if(key in self.checker_dict):
                new_dict[key]=self.checker_dict[key]
        return DictChecker(new_dict,self.optional,self.unlimit,self.allow_none)
        
    def get_params_dict(self,params_list,function_params_list):
        params_dict={}
        current_index=0
        dict_keys=list(self.checker_dict.keys())
        for params_name in function_params_list:
            if(current_index>=len(params_list)):
                return params_dict
            if(params_name in dict_keys):
                params_dict[params_name]=params_list[current_index]
                current_index+=1
        if(current_index<len(params_list)):
            self.report_error("The parameters is more than the dict defines")
        return params_dict


    def get_element_checker(self,key,node):
        if(key not in self.checker_dict.keys()):
            return None
        return self.checker_dict[key]


class ParamsChecker(DictChecker):
    def __init__(self,checker_list=[],optional=[]):
        self.checker_list=checker_list
        self.optional_index_store=[]
        super(ParamsChecker,self).__init__({},optional,False,False)
    
    def generate_params_dict(self,func,object_name):
        sort_list=None
        if(not isfunction(func)):
            if(isinstance(func,type)):
                func=func.__init__
                sort_list=list(func.__code__.co_varnames)[1:]
            else:
                raise ReigistError("The registed object '"+object_name+"' is not callable, the checker should not been registered")
        else:
            sort_list=list(func.__code__.co_varnames)

        if(len(sort_list)<len(self.checker_list)):
            raise ReigistError("The number of checkers is more than the number of params for the registed object '"+object_name+"'")

        for i in range(0,len(self.checker_list)):
            param=sort_list[i]
            self.checker_dict[param]=self.checker_list[i]

        for index in self.optional_index_store:
            self.optional.append(sort_list[index])

        new_dict_list=list(self.checker_dict.keys())
        for opt in self.optional:
            if(opt not in new_dict_list):
                raise ReigistError("The "+str(opt)+" doesn't appear in dict key for the registed object '"+object_name+"'")

    def add_checker(self,checker,optional=False):
        self.checker_list.append(checker)
        if(optional):
            self.optional_index_store.append(len(self.checker_list)-1)
    


class BaseListChecker(Checker):
    def __init__(self):
        pass

    def get_element_checker(self,index,node):
        raise NotImplementedError("The function need to be implemented")
 

#the list checker for check list
class ListChecker(BaseListChecker):
    def __init__(self,element_checker=None,max_numbers=-1,allow_none=False):
        super(ListChecker,self).__init__()
        self.element_checker=element_checker
        self.max_numbers=max_numbers
        self.allow_none=allow_none
    
    def check(self,node,node_root):
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

    
    def _check_single_before(self,element,output_root):
        if(self.element_checker is None):
            return True
        try:
            self.element_checker._check(element,output_root,self.location)
            return True
        except:
            return False
    
        
    def get_element_checker(self,index,node):
        return self.element_checker


#EnumChecker
class EnumChecker(Checker):
    def __init__(self,enums=[]):
        super(EnumChecker,self).__init__()
        self.enums=enums
        if(not isinstance(enums,list)):
            raise RuntimeError("The enum must be a list")
        for i in range(0,len(self.enums)):
            item=enums[i]
            if(item is None):
                continue
            if(isinstance(item,(float,int,str,bool,type(None),ObjectName))):
                continue
            raise RuntimeError("Unsupport value in enumeration")
            
    
    def check(self,node,node_root):
        node=node.value
        if(isinstance(node,(int,str,float,bool,type(None)))):
            if(node in self.enums):
                return
            else:
                display_value=""
                if(isinstance(node,str)):
                    display_value+="'"
                    display_value+=str(node)
                    display_value+="'"
                else:
                    display_value=str(node)
                self.report_error("The value "+display_value+" not in the enumeration")
        if(not isinstance(node,regist_object.RegistObject) or node.scope!="name"):
            self.report_error("The unsupport input type for enum")
        
        obj_name=node.object_name
        for i in range(0,len(self.enums)):
            item=self.enums[i]
            if(isinstance(item,ObjectName)):
                if(item.object_name==obj_name):
                    if(node.params is not None and item.instance):
                        return
                    if(node.params is None and not item.instance):
                        return
        
        self.report_error("The object '"+obj_name+"' not in the enumeration or the instance condition is wrong")

class BasicEnumChecker(EnumChecker):
    def __init__(self,enums=[]):
        if(not isinstance(enums,list)):
            raise RuntimeError("The enum must be a list")
        for item in enums:
            if(not isinstance(item,(int,float,bool,str,type(None)))):
                raise RuntimeError("The BasicEnumChecker just accepts the basic type: int, float, bool, str and None")
        super(BasicEnumChecker,self).__init__(enums)
    
    def check(self,node,node_root):
        value=node.value
        if(not isinstance(value,(int,float,bool,str,type(None)))):
            raise RuntimeError("The BasicEnumChecker just accepts the basic type: int, float, bool, str and None")
        super(BasicEnumChecker,self).check(node,node_root)

class ObjectEnumChecker(EnumChecker):
    def __init__(self,enums=[],instance=True):
        if(not isinstance(enums,list)):
            raise RuntimeError("The enum must be a list")
        obj_enums=[]
        for item in enums:
            if(not isinstance(item,str)):
                raise RuntimeError("The Object Name must be string")
            obj_enums.append(ObjectName(item,instance))
        super(ObjectEnumChecker,self).__init__(obj_enums)
    
    def check(self,node,node_root):
        value=node.value
        if(not isinstance(value,regist_object.RegistObject)):
            raise RuntimeError("The ObjectEnumChecker just accepts the type Object")
        super(ObjectEnumChecker,self).check(node,node_root)
        

        


