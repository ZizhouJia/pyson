# -*- coding: UTF-8 -*-
from antlr4 import *
from pyonLexer import pyonLexer
from pyonParser import pyonParser
from pyonListener import pyonListener
input_file="input.pyon"
input=FileStream(input_file,encoding='utf-8')
lexer=pyonLexer(input)
token_stream=CommonTokenStream(lexer)
parser=pyonParser(token_stream)
tree=parser.entry_point()
listener=pyonListener()
# tree_str=tree.toStringTree(recog=parser)
walker=ParseTreeWalker()
walker.walk(listener,tree)
print(listener.global_dict)