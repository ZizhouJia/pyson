class checker(object):
    def __init__(self):
        self.default=None

    def check(self,node,ctx):
        pass

    def tips(self):
        pass

    def default(self):
        return 

class int_checker(checker):
    def __init__(self,min_value=None,max_value=None,default=None):
        self.min_value=min_value
        self.max_value=max_value
        self.default=default
    
    def check(self,node,ctx):
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

