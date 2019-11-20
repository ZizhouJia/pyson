# Generated from pyson.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pysonParser import pysonParser
else:
    from pysonParser import pysonParser


from collections import OrderedDict
from . import regist_object

# This class defines a complete listener for a parse tree produced by pysonParser.
class pysonListener(ParseTreeListener):
    def __init__(self):
        super(pysonListener,self).__init__()
        self.return_value=None
        self._element_number=0
    
    def set_value(self,value_type,value,token):
        cont=regist_object.Content(value_type,value,self._element_number,token.symbol.line,token.symbol.column)
        self._element_number+=1
        return cont

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
        ctx.return_value=ctx.return_value=self.set_value(dict,ctx.items().return_value,ctx.LEFT_DICT())


    # Enter a parse tree produced by pysonParser#items.
    def enterItems(self, ctx:pysonParser.ItemsContext):
        pass

    # Exit a parse tree produced by pysonParser#items.
    def exitItems(self, ctx:pysonParser.ItemsContext):
        if(ctx.item() is None):
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
            token=ctx.TRUE()
            ctx.return_value=self.set_value(bool,True,token)
            return
        if(ctx.FALSE() is not None):
            token=ctx.FALSE()
            ctx.return_value=self.set_value(bool,False,token)
            return
        if(ctx.NONE() is not None):
            token=ctx.NONE()
            ctx.return_value=self.set_value(None,None,token)
            return
        if(ctx.INT() is not None):
            token=ctx.INT()
            ctx.return_value=self.set_value(int,int(str(ctx.INT().getText())),token)
            return
        if(ctx.FLOAT() is not None):
            token=ctx.FLOAT()
            ctx.return_value=self.set_value(float,float(str(ctx.FLOAT().getText())),token)
            return
        if(ctx.STRING() is not None):
            token=ctx.STRING()
            ctx.return_value=self.set_value(str,str(ctx.STRING())[1:-1],token)
            return
        if(ctx.SELF() is not None):
            token=ctx.SELF()
            ctx.return_value=self.set_value(regist_object.RegistObject,regist_object.RegistObject("","self",None),token)
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
        ctx.return_value=ctx.return_value=self.set_value(list,ctx.values().return_value,ctx.LEFT_LIST())


    # Enter a parse tree produced by pysonParser#item_tuple.
    def enterItem_tuple(self, ctx:pysonParser.Item_tupleContext):
        pass

    # Exit a parse tree produced by pysonParser#item_tuple.
    def exitItem_tuple(self, ctx:pysonParser.Item_tupleContext):
        ctx.return_value=self.set_value(list,ctx.values().return_value,ctx.LEFT_BUKKET())


    # Enter a parse tree produced by pysonParser#item_object.
    def enterItem_object(self, ctx:pysonParser.Item_objectContext):
        pass

    # Exit a parse tree produced by pysonParser#item_object.
    def exitItem_object(self, ctx:pysonParser.Item_objectContext):
        object_name=ctx.object_name().return_value.getText()
        scope=None
        name=None
        if('@' in object_name):
            scope="name"
            name=object_name[1:]
        elif("self" in object_name):
            scope="self"
            name=object_name[5:]
        else:
            scope="import"
            name=object_name

        if(ctx.item_dict() is not None):
            ctx.return_value=self.set_value(regist_object.RegistObject,regist_object.RegistObject(name,scope,ctx.item_dict().return_value),
            ctx.object_name().return_value)
            return
        if(ctx.item_tuple() is not None):
            ctx.return_value=self.set_value(regist_object.RegistObject,regist_object.RegistObject(name,scope,ctx.item_tuple().return_value),
            ctx.object_name().return_value)
            return
        ctx.return_value=self.set_value(regist_object.RegistObject,regist_object.RegistObject(name,scope,None),
            ctx.object_name().return_value)

    # Enter a parse tree produced by pysonParser#object_name.
    def enterObject_name(self, ctx:pysonParser.Object_nameContext):
        pass

    # Exit a parse tree produced by pysonParser#object_name.
    def exitObject_name(self, ctx:pysonParser.Object_nameContext):
        if(ctx.OBJECT() is not None):
            ctx.return_value=ctx.OBJECT()
            return
        if(ctx.KEY() is not None):
            ctx.return_value=ctx.KEY()
            return