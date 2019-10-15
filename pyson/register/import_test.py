import os
import importlib
import json

lib = importlib.import_module("importlib")
path=lib.__getattribute__("reload")
path
print(path)
try:
    wrong=lib.__getattribute__("wrong")
except:
    print("the wrong error")

d={"good":1,"bad":2}
d["bad"]=d
print(id(d))
print(id(d["bad"]))
print(d)


