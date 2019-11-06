# -*- coding: utf-8 -*-  
import os
import importlib
import pkgutil

from pyson.error import pyson_error

#change the register
class register(object):
    def __init__(self):
        self.regist_object={}
        self.package_load_allow=True
    
    def regist(self,object_name,obj,scheme=None):
        if(object_name in self.regist_object.keys()):
            raise pyson_error.ReigistError("The "+str(object_name)+" has already been used")
        self.regist_object[object_name]=[obj,scheme]
    
    def set_scheme(self,object_name,scheme):
        if(object_name not in self.regist_object.keys()):
            raise pyson_error.ReigistError("The "+str(object_name)+" is not been registed")
        self.regist_object[object_name][1]=scheme
        
    def get_object(self,object_name):
        if(object_name not in self.regist_object.keys()):
            return None
        return self.regist_object[object_name]
    
    def load_package_object(self,object_name):
        if(not self.package_load_allow):
            return None
        module_list=object_name.split('.')
        try:
            package=importlib.import_module(module_list[0])
            for i in range(1,len(module_list)):
                package=package.__getattribute__(module_list[i])
            return package
        except:
            return None



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




        



    
    
    

        
        