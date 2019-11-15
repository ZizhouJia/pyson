import time

starttime = time.time()
import pyson
endtime = time.time()
print("pyson load %.8f"%(endtime-starttime))
import os
from pyson.checker import *
from pyson import reg

starttime=time.time()
import torch.nn as nn
endtime = time.time()
print("pyson load %.8f"%(endtime-starttime))

@reg.regist("nn.sequential")
def sequential(nn_list):
    return nn.Sequential(*nn_list)

reg.regist_object("nn.conv2d",nn.Conv2d)

checkers=pyson.from_file("scheme.pyson")

for item in checkers:
    name=item["name"]
    checker=item["checker"]
    reg.set_params_checker(name,checker)


#Dict define the checker
pyson_checker={
    "model":ObjectChecker("nn.sequential"),
    "lr":FloatChecker(),
    "dataset":{
        "name":StringChecker(),
        "batch_size":IntChecker()
    },
    "array":ListChecker(),
    "another":None
}


reg.regist_checker("nn_solver",pyson_checker)


print(reg)


starttime=time.time()
result=pyson.from_file("input.pyon","nn_solver")
endtime = time.time()
print("pyson load %.8f"%(endtime-starttime))
print(result)
# print(result["another"])


# result=pyson.to_object(result)
# print(result)