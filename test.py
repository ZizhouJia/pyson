import pyson
import os
from pyson.checker import *
from pyson import reg
import torch.nn as nn

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
    }
}


reg.regist_checker("nn_solver",pyson_checker)

print(reg)


result=pyson.from_file("input.pyon","nn_solver")
print(result)
# result=pyson.to_object(result)
# print(result)