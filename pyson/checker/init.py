#-*-coding:utf-8 -*-
import pyson.regist as regist
import pyson.transform as transform
from . import checker

import os

def regist_checker():
    reg=regist.reg
    reg.regist("int",checker.int_checker,scope="checker")
    reg.regist("float",checker.float_checker,scope="checker")
    reg.regist("string",checker.string_checker,scope="checker")
    reg.regist("bool",checker.bool_checker,scope="checker")
    reg.regist("none",checker.none_checker,scope="checker")
    reg.regist("ctx",checker.ctx_checker,scope="checker")
    reg.regist("object_name",checker.object_name_checker,scope="checker")
    reg.regist("object",checker.object_checker,scope="checker")
    reg.regist("dict",checker.dict_checker,scope="checker")
    reg.regist("list",checker.list_checker,scope="checker")
    reg.regist("enum",checker.enum_checker,scope="checker")

def regist_checker_scheme():
    reg=regist.reg
    current_path=os.path.abspath(__file__)
    father_path=os.path.abspath(os.path.dirname(current_path)+os.path.sep+".")
    file_name=os.path.join(father_path,"checker_scheme.pyson")
    scheme_list=transform.from_file(file_name)
    for i in range(0,len(scheme_list)):
        scheme_dict=scheme_list[i]
        reg.set_scheme(scheme_dict["name"],scheme_dict["scheme"],"checker")

regist_checker()
regist_checker_scheme()


#理顺一下import关系
#error是一个单独的引用，不依赖于任何项
#regist是一个单独的引用，不依赖于任何项，可以随意引用
#transform依赖regist中的reg和pyson(parser listener以及pyson_object)
#checker是一个单独的引用，不依赖于任何项，可以随意引用
#ErrorException放置在checker中，但是在transform中也会用到这一项，在这里我应该单独把这一项抽取出来





