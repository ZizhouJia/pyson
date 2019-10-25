import os
import importlib
import pkgutil
class register(object):
    def __init__(self):
        self.regist_object={}
        self.regist_solver={}
        self.regist_object["default"]={}
    
    def regist(self,object_name,obj,scheme=None,scope="default"):
        if(scope in ["import"]):
            return False
        if(scope not in self.regist_object.keys()):
            self.regist_object[scope]={}
        self.regist_object[scope][object_name]=(obj,scheme)
    
    def regist_sovler(self,sovler_name,scheme=None,scope="default"):
        if(scope in ["import"]):
            return False
        if(scope not in self.regist_solver.keys()):
            self.regist_solver[scope]={}
        self.regist_solver[scope][sovler_name]=scheme
    
    def _load_package(self,module_list):
        try:
            package=importlib.import_module(module_list[0])
            for i in range(1,len(module_list)):
                package=package.__getattribute__(module_list[i])
            return package
        except:
            return None
        
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


        



    
    
    

        
        