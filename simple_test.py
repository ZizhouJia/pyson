from inspect import isfunction
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def B(a=1):
    return a

# print(A.__init__.__code__.co_varnames)
# print(type(A.__init__))
# print(type(A(1,2)))
# print(type(1))
# print(isinstance(A(1,2),type))
# print(isinstance(A,type))

# print(B)
# print(type(B))

# print(isfunction(A))
# print(isfunction(B))
a=None
print(isinstance(a,type(None)))

dict