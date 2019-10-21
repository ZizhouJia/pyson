import re
class checker(object):
    def __init__(self):
        self.default=None

    def check(self,node,ctx):
        pass

    def tips(self):
        pass

    def get_default(self):
        return self.default

class int_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=None,allow_none=False):
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
        if(self.default is not None and not self.check(default)):
            raise RuntimeError("The defualt value is wrong "+str(default))

    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return True
        if(not isinstance(node,int)):
            return False
        if(self.min_value is not None):
            if(node<self.min_value):
                return False
        if(self.max_value is not None):
            if(node>self.max_value):
                return False
        return True
    
    def tips(self):
        return []

class float_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=None,allow_none=False):
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
        self.allow_none=allow_none
        if(self.default is not None and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return True
        if(not isinstance(node,(int,float))):
            return False
        if(self.min_value is not None):
            if(node<self.min_value):
                return False
        if(self.max_value is not None):
            if(node>self.max_value):
                return False
        return True
    
    def tips(self):
        return []

class string_checker(checker):
    def __init__(self,pattern=None,default=None,allow_none=False):
        self.pattern=pattern
        self.default=default
        self.allow_none=allow_none
        if(self.default is not None and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))

    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return True
        if(not isinstance(node,str)):
            return False
        if(self.pattern is not None and re.match(self.pattern,node) is None):
            return False
        return True

class bool_checker(checker):
    def __init__(self,default=None,allow_none=False):
        self.default=default
        self.allow_none=allow_none
        if(self.default is not None and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(node is None and self.allow_none):
            return True
        if(not isinstance(node,bool)):
            return True
        return False
    
class none_checker(checker):
    def __init__(self):
        pass

    def check(self,node,ctx):
        if(node is None):
            return True
        return False

class ctx_checker(checker):
    def __init__(self):
        pass

    def check(self,node,ctx):
        if(isinstance(node,tuple)):
            if(node[0]=="ctx"):
                return True
        return False

class object_checker(checker):
    def __init__(self,pattern=None,default=None):
        self.pattern=pattern
        self.default=default
        if(self.default is not None and not self.check(default,None)):
            raise RuntimeError("The defualt value is wrong "+str(default))
    
    def check(self,node,ctx):
        if(isinstance(node,tuple)):
            
        
        
        
        
            
        

