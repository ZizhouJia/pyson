#-*-coding:utf-8 -*-
import pyson.transform as transform
import pyson.checker as checker
import pyson.regist as regist

import os

def regist_checker():
    
    reg=regist.reg
    reg.regist_object("IntChecker",checker.IntChecker)
    reg.regist_object("FloatChecker",checker.FloatChecker)
    reg.regist_object("StringChecker",checker.StringChecker)
    reg.regist_object("BoolChecker",checker.BoolChecker)
    reg.regist_object("NoneChecker",checker.NoneChecker)
    reg.regist_object("SelfChecker",checker.SelfChecker)
    reg.regist_object("ObjectChecker",checker.ObjectChecker)
    reg.regist_object("DictChecker",checker.DictChecker)
    reg.regist_object("ListChecker",checker.ListChecker)
    reg.regist_object("EnumChecker",checker.EnumChecker)
    reg.regist_object("ParamsChecker",checker.ParamsChecker)

def regist_checker_scheme():
    reg=regist.reg
    current_path=os.path.abspath(__file__)
    father_path=os.path.abspath(os.path.dirname(current_path)+os.path.sep+".")
    file_name=os.path.join(father_path,"checker_scheme.pyson")
    scheme_list=transform.from_file(file_name)
    for i in range(0,len(scheme_list)):
        scheme_dict=scheme_list[i]
        reg.set_params_checker(scheme_dict["name"],scheme_dict["scheme"])

regist_checker()
regist_checker_scheme()


#理顺一下import关系
#error是一个单独的引用，不依赖于任何项
#regist是一个单独的引用，不依赖于任何项，可以随意引用
#transform依赖regist中的reg和pyson(parser listener以及pyson_object)
#checker是一个单独的引用，不依赖于任何项，可以随意引用
#ErrorException放置在checker中，但是在transform中也会用到这一项，在这里我应该单独把这一项抽取出来





