
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir+"/..")

import pyon
from antlr4 import *
from pyon.pyonLexer import pyonLexer
from pyon.pyonParser import pyonParser
from pyon.pyonListener import pyonListener

import regiser
import regiser.transform
import regiser.register

reg=regiser.register.reg
#test solver 

trans= regiser.transform.transform(regiser.register.reg)



input_file="input.pyon"
input=FileStream(input_file,encoding='utf-8')
print(input)
lexer=pyonLexer(input)
token_stream=CommonTokenStream(lexer)
parser=pyonParser(token_stream)
tree=parser.entry_point()
listener=pyonListener()
# tree_str=tree.toStringTree(recog=parser)
walker=ParseTreeWalker()
walker.walk(listener,tree)
d=listener.global_dict

result=trans.transfrom(d)
print(result)




