class RegistObject(object):
    def __init__(self,object_name,scope=None,params=None):
        self.object_name=object_name
        self.scope=scope
        self.params=params

class RegistObjectName(object):
    def __init__(self,object_name,scope=None):
        self.object_name=object_name
        self.scope=scope

class Content(object):
    def __init__(self,type,value,element_number,line=0,column=0):
        self.type=type
        self.value=value
        self.element_number=element_number
        self.line=line
        self.column=column