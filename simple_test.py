class ReadOnlyDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self,*args,**kwargs)
        self.__dict__ = self
    
    def __setitem__(self,k,v):
        raise RuntimeError("The dict is read only")
    
    def __delitem__(self,k):
        raise RuntimeError("The dict is read only")

    # def __setattr__(self,k,v):
    #     raise RuntimeError("The dict item can not been changed")

    # def __delattr__(self,k):
    #     raise RuntimeError("The dict item can not been changed")

class ReadOnlyList(list):
    def __init__(self,value=[]):
        if(not isinstance(value,list)):
            raise RuntimeError("The input must be the instance of the list")
        list.__init__(value)
    
    def append(self,obj):
        raise RuntimeError("The list is read only")

    def extend(self,obj):
        raise RuntimeError("The list is read only")

    def insert(self,index,obj):
        raise RuntimeError("The list is read only")

    def pop(self,obj):
        raise RuntimeError("The list is read only")

    def remove(self,obj):
        raise RuntimeError("The list is read only")

    def reverse(self,obj):
        raise RuntimeError("The list is read only")

    def sort(self,obj):
        raise RuntimeError("The list is read only")

    def __setitem__(self,k,v):
        raise RuntimeError("The list is read only")

    def __delitem__(self,k):
        raise RuntimeError("The list is read only")

def convert_read_only(input):
    if(isinstance(input,dict)):
        d={}
        for key in input.keys():
            d[key]=convert_read_only(input[key])
        return ReadOnlyDict(d)
    if(isinstance(input,list)):
        l=[]
        for value in input:
            l.append(convert_read_only(value))
        return ReadOnlyList(l)
    return input
    
    


# d={"a":1,"b":2}

# rd=ReadOnlyDict(d)
# print(rd)
# del rd["a"]
# print(rd)
# rd["c"]=1
# rd["a"]=2


# l=ReadOnlyList([1,2,3,4,5])
# class prv(object):
#     def __init__(self):
#         self.__name=1

# p=prv()
# print(p.__name)