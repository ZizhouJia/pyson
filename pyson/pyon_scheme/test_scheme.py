# -*- coding: UTF-8 -*-
from antlr4 import *
from pyonSchemeLexer import pyonSchemeLexer
from pyonSchemeParser import pyonSchemeParser

input_file="input.pyon"
input=FileStream(input_file,encoding='utf-8')
print(input)
lexer=pyonSchemeLexer(input)
token_stream=CommonTokenStream(lexer)
parser=pyonSchemeParser(token_stream)
tree=parser.entry_point()
tree_str=tree.toStringTree(recog=parser)
print(tree_str)

