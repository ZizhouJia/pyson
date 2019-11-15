# -*- coding: utf-8 -*-  
import os
import importlib
import pkgutil
from collections import OrderedDict

from pyson.error import pyson_error
import pyson.checker as c

#change the register
class Register(object):
    def __init__(self):
        self._regist_object=OrderedDict()
        self._regist_pyson_checker=OrderedDict()
        self.package_load_allow=True
    
    def regist_object(self,object_name,obj,checker=None):
        if(object_name in self._regist_object.keys()):
            raise pyson_error.ReigistError("The "+str(object_name)+" has already been used")
        self._regist_object[object_name]=[obj,None]
        if(checker is not None):
            self.set_params_checker(object_name,checker)
    
    def set_params_checker(self,object_name,checker):
        if(object_name not in self._regist_object.keys()):
            raise pyson_error.ReigistError("The "+str(object_name)+" is not been registed")
        func=self.get_object(object_name)[0]
        new_checker=None
        if(isinstance(checker,dict)):
            new_checker=c.DictChecker(checker)
        elif(isinstance(checker,(c.DictChecker,c.ParamsChecker))):
            new_checker=checker
        else:
           raise RuntimeError("The checker type is wrong")
        new_checker._sort_params_key(func)
        self._regist_object[object_name][1]=new_checker

        self._regist_object[object_name][1]=checker
        
    def get_object(self,object_name):
        if(object_name not in self._regist_object.keys()):
            return None
        return self._regist_object[object_name]
    
    def load_package_object(self,object_name):
        if(not self.package_load_allow):
            return None
        module_list=object_name.split('.')
        if(len(module_list)==1):
            builtin=globals()["__builtins__"]
            if(module_list[0] in builtin):
                return builtin[module_list[0]]
        try:
            package=importlib.import_module(module_list[0])
            for i in range(1,len(module_list)):
                package=package.__getattribute__(module_list[i])
            return package
        except:
            return None
    
    def regist(self,object_name,checker=None):
        def iner_warper(func):
            self.regist_object(object_name,func,checker)
        return iner_warper
    
    def regist_checker(self,name,checker):
        import pyson.checker as c
        if(name not in self._regist_pyson_checker):
            if(not isinstance(checker,(dict,c.DictChecker,c.ListChecker))):
                raise RuntimeError("The checker type is wrong")
            self._regist_pyson_checker[name]=checker
        else:
            raise pyson_error.ReigistError("The "+str(name)+" has already been registed")
    
    def get_checker(self,name):
        if(name not in self._regist_pyson_checker):
            return None
        return self._regist_pyson_checker[name]
    
    def __str__(self):
        output=""
        output+=" regist function:\n"
        for key in self._regist_object.keys():
            output+=("  @"+str(key)+"\n")
        output+=" regist pyson checker:\n"
        for key in self._regist_pyson_checker.keys():
            output+=("  -"+str(key)+"\n")
        return output



reg=Register()

#checker代表了一组预先定义好的函数检测器
#scheme代表了checker的实例，用于检测函数的参数格式，或是检测pyson_object的格式


#从最基本的开始
#首先是定义checker的scheme，这一组scheme也是使用checker来进行定义，这个时候checker都没有约束性scheme，checker可以任意指定
#然后将checker和对应的scheme都注册到regist中去
#然后再注册pyson_object的scheme，使用




        



    
    
    

        
        