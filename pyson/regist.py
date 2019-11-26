# -*- coding: utf-8 -*-  
import os
import importlib
import pkgutil
from collections import OrderedDict

from pyson.error import ReigistError
import pyson.checker as c

#change the register
class Register(object):
    def __init__(self):
        self._regist_object=OrderedDict()
        self._regist_pyson_checker=OrderedDict()
        self.package_load_allow=True
    
    def regist_object(self,object_name,obj,checker=None):
        if(object_name in self._regist_object.keys()):
            raise ReigistError("The "+str(object_name)+" has already been used")
        self._regist_object[object_name]=[obj,None]
        if(checker is not None):
            self.set_params_checker(object_name,checker)
    
    def set_params_checker(self,object_name,checker):
        if(object_name not in self._regist_object.keys()):
            raise ReigistError("The "+str(object_name)+" is not been registed")
        func=self.get_object(object_name)[0]
        if(isinstance(checker,c.ParamsChecker)):
            checker.generate_params_dict(func,object_name)
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
        if(name not in self._regist_pyson_checker):
            self._regist_pyson_checker[name]=checker
        else:
            raise ReigistError("The "+str(name)+" has already been registed")

        
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
            output+=("  @"+str(key)+"\n")
        return output

reg=Register()




        



    
    
    

        
        