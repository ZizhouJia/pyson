# PySON
A JSON like more powerful notation for python

## Introduction
PySON is a JSON like object notation for python. Besides the usual use of the JSON, the python class and the function call can be represented with PySON which can be dynamically parsed into the python object at the running time. The checker is also aviliable for the PySON.

## Install
pip install python-pyson

## Getting Started
### Basic Type
Likes the JSON object, The PySON object is also nested with the dict and the list.  
The value can be int, float, bool, string four types.
The PySON object is like following:
//suppose the PySON object saved in the input.pyson file
{
    school:"Tsinghua",
    city:"Beijing"
    students:
    [
        {
            name:'Tom',
            age:18,
            height:1.78,
            male:true,
            introduction:none,
            friends:["Harry","Danny","Neo"]
        }
    ]
}
Different with the JSON, the key don't have the " , and composed with the [A-Za-z_] and [0-9].
Likes the _var1 name_var2 a831239 and so on.  
The PySON can be parsed into the dict in python
likes following:
import pyson
pyson_object=pyson.from_file("input.pyson")
print(pyson_object["school"])
print(pyson_object["student"][0]["name"])
The data can also be accessed with the dot.
pyson_object["student"][0]["name"] is as the same as the output.student[0].name
### The Regist Object Type
Different with JSON, The Python object, class and function call can be represented with the PySON. Here we use regist object type to name this representation.
First we have to regist the object on the pyson register.
Suppose we have a Student class, defined as :
class Student(object):
    def __init__(self,name,age,height,male,introduction,friends):
        self.name=name
        self.age=age
        self.height=height
        self.male=male
        self.introduction=introduction
        self.friends=friends
Then we regist the class:
import pyson
pyson.reg.regist_object("Student",Student)

the @reg.regist("Student") decorator can also been used to regist the class and the function 

The PySON object can be like this:
{
    school:"Tsinghua",
    city:"Beijing"
    students:
    [
        @Student{
            name:'Tom',
            age:18,
            height:1.78,
            male:true,
            introduction:none,
            friends:["Harry","Danny","Neo"]
        }
    ]
}
The regist object in pyson begin with '@' following the regist object name. The parameters can be represented with a dict. The key is the parameter name and the value is the actual value we pass into the callee function.
The param name can also be ignored, the object 'Student' can be written as the following:
@Student('Tom',18,1.78,true,none,["Harry","Danny","Neo"])
likes the PySON object before, it can also parsed into the python dict with the from_file method
import pyson
pyson_object=pyson.from_file("input.pyson")
print(pyson_object)
### The Module Object Type  
The PySON object can also call the Python package and the buildin function.  
Here we use the module object to name this representation.
Different with the regist object, the moudule object don't have to be registed, the python package and buildin function can directly called with the origin package name and function name.
{
    array:numpy.Array([1,2,3,4,5]),
    length:len(array)
}
import pyson
pyson_object=pyson.from_file("input.pyson")
print(pyson_object)  
Sometimes, It may be dangerous for directly calling the python package and the buildin function.
It can be disabled with following code:  
pyson.reg.package_load_allow=False,  
the package and buildin function will not been found.

### The Self Keyward Reference
We can use the self keyward to reference the key which has already defined before.  
The corresponding value of the key will be copied and assign to the current key which uses the self keyward reference. The actually python object will not been copied, it just store the pointer of the origin python object (shallow copy) and the basic type (int,float,bool,string,dict,list) will be copied recursively (deep copy)
given the PySON dict:
{
    students:["Tom","Danny","Neo","Tom"],
    selected_student:self.students.1
}
the selected_student is "Danny"  
Anther example show the self keyward reference copy mechanism is here:
{
    school_info:{
        school_name:"Tsinghua",
        student:@Student{
            name:'Tom',
            age:18,
            height:1.78,
            male:true,
            introduction:none,
            friends:["Harry","Danny","Neo"]
        }
    }
    modified_info:@modify_info{
        input_dict:self.school_info,
        school_name:"THU",
        age:19
    }
}

@reg.regist("modify_info")
def modify_info(input_dict,school_name,age):
    input_dict["school_name"]=school_name
    input_dict["student"].age=age
    return input_dict

print(pyson_object.school_name)
print(pyson_object.student)










