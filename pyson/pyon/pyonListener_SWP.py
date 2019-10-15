# Generated from pyon.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pyonParser import pyonParser
else:
    from pyonParser import pyonParser

from collections import OrderedDict

# This class defines a complete listener for a parse tree produced by pyonParser.
class pyonListener(ParseTreeListener):
    def __init__(self,register):
        super(pyonListener,self).__init__()
        self.global_dict=OrderedDict()
        self.local_variable={}
        self.register=register


    # Enter a parse tree produced by pyonParser#entry_point.
    def enterEntry_point(self, ctx:pyonParser.Entry_pointContext):
        ctx.prefix=""

    # Exit a parse tree produced by pyonParser#entry_point.
    def exitEntry_point(self, ctx:pyonParser.Entry_pointContext):
        self.global_dict=ctx.item_dict().return_value


    # Enter a parse tree produced by pyonParser#item_dict.
    def enterItem_dict(self, ctx:pyonParser.Item_dictContext):
        pass

    # Exit a parse tree produced by pyonParser#item_dict.
    def exitItem_dict(self, ctx:pyonParser.Item_dictContext):
        ctx.return_value=ctx.items().return_value


    # Enter a parse tree produced by pyonParser#items.
    def enterItems(self, ctx:pyonParser.ItemsContext):
        pass

    # Exit a parse tree produced by pyonParser#items.
    def exitItems(self, ctx:pyonParser.ItemsContext):
        if(ctx.isEmpty()):
            ctx.return_value=OrderedDict()
            return
        item_value=ctx.item().return_value
        others_value=ctx.other_items().return_value
        item_value.update(others_value)
        ctx.return_value=item_value

    # Enter a parse tree produced by pyonParser#other_items.
    def enterOther_items(self, ctx:pyonParser.Other_itemsContext):
        pass

    # Exit a parse tree produced by pyonParser#other_items.
    def exitOther_items(self, ctx:pyonParser.Other_itemsContext):
        if(ctx.item() is None):
            ctx.return_value=OrderedDict()
            return
        item_value=ctx.item().return_value
        other_value=ctx.other_items().return_value
        item_value.update(other_value)
        ctx.return_value=item_value

    # Enter a parse tree produced by pyonParser#item.
    def enterItem(self, ctx:pyonParser.ItemContext):
        pass

    # Exit a parse tree produced by pyonParser#item.
    def exitItem(self, ctx:pyonParser.ItemContext):
        ctx.return_value=OrderedDict()
        ctx.return_value[str(ctx.KEY())]=ctx.value().return_value



    # Enter a parse tree produced by pyonParser#value.
    def enterValue(self, ctx:pyonParser.ValueContext):
        pass

    # Exit a parse tree produced by pyonParser#value.
    def exitValue(self, ctx:pyonParser.ValueContext):
        if(ctx.TRUE() is not None):
            ctx.return_value=True
            return
        if(ctx.FALSE() is not None):
            ctx.return_value=False
            return
        if(ctx.NONE() is not None):
            ctx.return_value=None
            return
        if(ctx.INT() is not None):
            ctx.return_value=int(str(ctx.INT().getText()))
            return
        if(ctx.FLOAT() is not None):
            ctx.return_value=float(str(ctx.FLOAT().getText()))
            return
        if(ctx.STRING() is not None):
            ctx.return_value=str(ctx.STRING())
            return
        if(ctx.item_dict() is not None):
            ctx.return_value=ctx.item_dict().return_value
            return
        if(ctx.item_list() is not None):
            ctx.return_value=ctx.item_list().return_value
            return
        if(ctx.item_object() is not None):
            ctx.return_value=ctx.item_object().return_value
            return


    # Enter a parse tree produced by pyonParser#values.
    def enterValues(self, ctx:pyonParser.ValuesContext):
        pass

    # Exit a parse tree produced by pyonParser#values.
    def exitValues(self, ctx:pyonParser.ValuesContext):
        if(ctx.value() is None):
            ctx.return_value=[]
            return
        item_value=[ctx.value().return_value]
        other_value=ctx.other_values().return_value
        item_value+=other_value
        ctx.return_value=item_value
        
    # Enter a parse tree produced by pyonParser#other_values.
    def enterOther_values(self, ctx:pyonParser.Other_valuesContext):
        pass

    # Exit a parse tree produced by pyonParser#other_values.
    def exitOther_values(self, ctx:pyonParser.Other_valuesContext):
        if(ctx.value() is None):
            ctx.return_value=[]
            return
        item_value=[ctx.value().return_value]
        other_value=ctx.other_values().return_value
        item_value+=other_value
        ctx.return_value=item_value

    # Enter a parse tree produced by pyonParser#item_list.
    def enterItem_list(self, ctx:pyonParser.Item_listContext):
        pass

    # Exit a parse tree produced by pyonParser#item_list.
    def exitItem_list(self, ctx:pyonParser.Item_listContext):
        ctx.return_value=ctx.values().return_value
        
    # Enter a parse tree produced by pyonParser#item_tuple.
    def enterItem_tuple(self, ctx:pyonParser.Item_tupleContext):
        pass

    # Exit a parse tree produced by pyonParser#item_tuple.
    def exitItem_tuple(self, ctx:pyonParser.Item_tupleContext):
        ctx.return_value=ctx.values().return_value


    # Enter a parse tree produced by pyonParser#item_object.
    def enterItem_object(self, ctx:pyonParser.Item_objectContext):
        pass

    # Exit a parse tree produced by pyonParser#item_object.
    def exitItem_object(self, ctx:pyonParser.Item_objectContext):
        object_name=ctx.OBJECT().getText()
        if(ctx.item_dict() is not None):
            ctx.return_value=(object_name,ctx.item_dict().return_value)
            return
        if(ctx.item_tuple() is not None):
            ctx.return_value=(object_name,ctx.item_tuple().return_value)
            return
        ctx.return_value=(object_name,None)
    




