# Generated from pyson.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pysonParser import pysonParser
else:
    from pysonParser import pysonParser

from collections import OrderedDict
from . import pyson_object

# This class defines a complete listener for a parse tree produced by pysonParser.
class pysonListener(ParseTreeListener):
    def __init__(self):
        super(pysonListener,self).__init__()
        self.return_value=None

    # Enter a parse tree produced by pysonParser#entry_point.
    def enterEntry_point(self, ctx:pysonParser.Entry_pointContext):
        pass

    # Exit a parse tree produced by pysonParser#entry_point.
    def exitEntry_point(self, ctx:pysonParser.Entry_pointContext):
        if(ctx.item_dict() is not None):
            self.return_value=ctx.item_dict().return_value
            return
        if(ctx.item_list() is not None):
            self.return_value=ctx.item_list().return_value
            return


    # Enter a parse tree produced by pysonParser#item_dict.
    def enterItem_dict(self, ctx:pysonParser.Item_dictContext):
        pass

    # Exit a parse tree produced by pysonParser#item_dict.
    def exitItem_dict(self, ctx:pysonParser.Item_dictContext):
        ctx.return_value=ctx.items().return_value


    # Enter a parse tree produced by pysonParser#items.
    def enterItems(self, ctx:pysonParser.ItemsContext):
        pass

    # Exit a parse tree produced by pysonParser#items.
    def exitItems(self, ctx:pysonParser.ItemsContext):
        if(ctx.isEmpty()):
            ctx.return_value=OrderedDict()
            return
        item_value=ctx.item().return_value
        others_value=ctx.other_items().return_value
        item_value.update(others_value)
        ctx.return_value=item_value

    # Enter a parse tree produced by pysonParser#other_items.
    def enterOther_items(self, ctx:pysonParser.Other_itemsContext):
        pass

    # Exit a parse tree produced by pysonParser#other_items.
    def exitOther_items(self, ctx:pysonParser.Other_itemsContext):
        if(ctx.item() is None):
            ctx.return_value=OrderedDict()
            return
        item_value=ctx.item().return_value
        other_value=ctx.other_items().return_value
        item_value.update(other_value)
        ctx.return_value=item_value


    # Enter a parse tree produced by pysonParser#item.
    def enterItem(self, ctx:pysonParser.ItemContext):
        pass

    # Exit a parse tree produced by pysonParser#item.
    def exitItem(self, ctx:pysonParser.ItemContext):
        ctx.return_value=OrderedDict()
        ctx.return_value[str(ctx.KEY())]=ctx.value().return_value


    # Enter a parse tree produced by pysonParser#value.
    def enterValue(self, ctx:pysonParser.ValueContext):
        pass

    # Exit a parse tree produced by pysonParser#value.
    def exitValue(self, ctx:pysonParser.ValueContext):
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
            ctx.return_value=str(ctx.STRING())[1:-1]
            return
        if(ctx.CTX() is not None):
            ctx.return_value=pyson_object.pyson_object("ctx",None)
            return
        if(ctx.OBJECT_NAME() is not None):
            text=str(ctx.OBJECT_NAME().getText())
            text=text.split('#')
            if(len(text[0])==0):
                text[0]="default"
            ctx.return_value=pyson_object.pyson_name(text[1],text[0])
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



    # Enter a parse tree produced by pysonParser#values.
    def enterValues(self, ctx:pysonParser.ValuesContext):
        pass

    # Exit a parse tree produced by pysonParser#values.
    def exitValues(self, ctx:pysonParser.ValuesContext):
        if(ctx.value() is None):
            ctx.return_value=[]
            return
        item_value=[ctx.value().return_value]
        other_value=ctx.other_values().return_value
        item_value+=other_value
        ctx.return_value=item_value


    # Enter a parse tree produced by pysonParser#other_values.
    def enterOther_values(self, ctx:pysonParser.Other_valuesContext):
        pass

    # Exit a parse tree produced by pysonParser#other_values.
    def exitOther_values(self, ctx:pysonParser.Other_valuesContext):
        if(ctx.value() is None):
            ctx.return_value=[]
            return
        item_value=[ctx.value().return_value]
        other_value=ctx.other_values().return_value
        item_value+=other_value
        ctx.return_value=item_value


    # Enter a parse tree produced by pysonParser#item_list.
    def enterItem_list(self, ctx:pysonParser.Item_listContext):
        pass

    # Exit a parse tree produced by pysonParser#item_list.
    def exitItem_list(self, ctx:pysonParser.Item_listContext):
        ctx.return_value=ctx.values().return_value


    # Enter a parse tree produced by pysonParser#item_tuple.
    def enterItem_tuple(self, ctx:pysonParser.Item_tupleContext):
        pass

    # Exit a parse tree produced by pysonParser#item_tuple.
    def exitItem_tuple(self, ctx:pysonParser.Item_tupleContext):
        ctx.return_value=ctx.values().return_value


    # Enter a parse tree produced by pysonParser#item_object.
    def enterItem_object(self, ctx:pysonParser.Item_objectContext):
        pass

    # Exit a parse tree produced by pysonParser#item_object.
    def exitItem_object(self, ctx:pysonParser.Item_objectContext):
        object_name=ctx.OBJECT().getText()
        object_name=object_name.split('@')
        if(len(object_name[0])==0):
            object_name[0]="default"
        if(ctx.item_dict() is not None):
            ctx.return_value=pyson_object.pyson_object(object_name[1],object_name[0],ctx.item_dict().return_value)
            return
        if(ctx.item_tuple() is not None):
            ctx.return_value=pyson_object.pyson_object(object_name[1],object_name[0],ctx.item_tuple().return_value)
            return
        ctx.return_value=pyson_object.pyson_object(object_name[1],object_name[0],None)