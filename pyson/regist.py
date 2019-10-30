# -*- coding: utf-8 -*-  
import os
import importlib
import pkgutil
class register(object):
    def __init__(self):
        self.regist_object={}
        self.regist_solver={}
        self.regist_object["default"]={}
    
    def regist(self,object_name,obj,scheme=None,scope="default"):
        if(scope in ["import","scheme"]):
            raise RuntimeError("The scope should not be import or scheme")
        if(scope not in self.regist_object.keys()):
            self.regist_object[scope]={}
        self.regist_object[scope][object_name]=(obj,scheme)
    
    def _load_package(self,module_list):
        try:
            package=importlib.import_module(module_list[0])
            for i in range(1,len(module_list)):
                package=package.__getattribute__(module_list[i])
            return package
        except:
            return None
    
    def set_scheme(self,object_name,scheme,scope="default"):
        if(scope not in self.regist_object.keys()):
            raise RuntimeError("The scope can not be found")
        object_dict=self.regist_object[scope]
        if(object_name not in object_dict):
            raise RuntimeError("The object is not resigted")
        object_dict[object_name][1]=scheme
        
    def get_object(self,object_name,scope):
        if(scope=="import"):
            others=object_name.split('.')
            package=self._load_package(others)
            if(package is None):
                return None
            return (package,None)
            
        if(scope not in self.regist_object.keys()):
            return None
        if(object_name not in self.regist_object[scope].keys()):
            return None
        return self.regist_object[scope][object_name]
    
    def load_sheme_from_file(self,file_path):
        pass

    def regist_scheme(self,scheme_name,scheme=None):
        if("scheme" not in self.regist_object.keys()):
            self.regist_object["scheme"]={}
        self.regist_object["scheme"][scheme_name]=(scheme,None)



class object_name_utils(object):
    @staticmethod
    def split_scope_name(object_name):
        if(object_name[0]=='@'):
            return "default",object_name[1:]
        else:
            result=object_name.split('@')
            return result[0],result[1]
    
    @staticmethod
    def parse_object_name(object_name):
        scope,name=object_name_utils.split_scope_name(object_name)
        return scope,name.split('.')

reg=register()

#checker代表了一组预先定义好的函数检测器
#scheme代表了checker的实例，用于检测函数的参数格式，或是检测pyson_object的格式


#从最基本的开始
#首先是定义checker的scheme，这一组scheme也是使用checker来进行定义，这个时候checker都没有约束性scheme，checker可以任意指定
#然后将checker和对应的scheme都注册到regist中去
#然后再注册pyson_object的scheme，使用




        



    
    
    

        
        