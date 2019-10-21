class pyson_object(object):
    def __init__(self,object_name,scope=None,params=None):
        self.object_name=object_name
        self.scope=scope
        self.params=params

class pyson_name(object):
    def __init__(self,object_name,scope=None):
        self.object_name=object_name
        self.scope=scope


