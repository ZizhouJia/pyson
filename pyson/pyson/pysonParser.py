# Generated from pyson.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\5\2\35\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\'\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7>\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\bD\n\b\3\t\3\t\3\t\3\t\3\t\5\tK\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r[")
        buf.write("\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\3\4\2")
        buf.write("\t\t\13\13\2`\2\34\3\2\2\2\4\36\3\2\2\2\6&\3\2\2\2\b-")
        buf.write("\3\2\2\2\n/\3\2\2\2\f=\3\2\2\2\16C\3\2\2\2\20J\3\2\2\2")
        buf.write("\22L\3\2\2\2\24P\3\2\2\2\26T\3\2\2\2\30V\3\2\2\2\32\35")
        buf.write("\5\4\3\2\33\35\5\22\n\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write("\3\3\2\2\2\36\37\7\16\2\2\37 \5\6\4\2 !\7\17\2\2!\5\3")
        buf.write("\2\2\2\"#\5\n\6\2#$\5\b\5\2$\'\3\2\2\2%\'\3\2\2\2&\"\3")
        buf.write("\2\2\2&%\3\2\2\2\'\7\3\2\2\2()\7\f\2\2)*\5\n\6\2*+\5\b")
        buf.write("\5\2+.\3\2\2\2,.\3\2\2\2-(\3\2\2\2-,\3\2\2\2.\t\3\2\2")
        buf.write("\2/\60\7\t\2\2\60\61\7\r\2\2\61\62\5\f\7\2\62\13\3\2\2")
        buf.write("\2\63>\7\3\2\2\64>\7\4\2\2\65>\7\5\2\2\66>\7\6\2\2\67")
        buf.write(">\7\7\2\28>\7\n\2\29>\7\b\2\2:>\5\4\3\2;>\5\22\n\2<>\5")
        buf.write("\30\r\2=\63\3\2\2\2=\64\3\2\2\2=\65\3\2\2\2=\66\3\2\2")
        buf.write("\2=\67\3\2\2\2=8\3\2\2\2=9\3\2\2\2=:\3\2\2\2=;\3\2\2\2")
        buf.write("=<\3\2\2\2>\r\3\2\2\2?@\5\f\7\2@A\5\20\t\2AD\3\2\2\2B")
        buf.write("D\3\2\2\2C?\3\2\2\2CB\3\2\2\2D\17\3\2\2\2EF\7\f\2\2FG")
        buf.write("\5\f\7\2GH\5\20\t\2HK\3\2\2\2IK\3\2\2\2JE\3\2\2\2JI\3")
        buf.write("\2\2\2K\21\3\2\2\2LM\7\20\2\2MN\5\16\b\2NO\7\21\2\2O\23")
        buf.write("\3\2\2\2PQ\7\22\2\2QR\5\16\b\2RS\7\23\2\2S\25\3\2\2\2")
        buf.write("TU\t\2\2\2U\27\3\2\2\2VZ\5\26\f\2W[\5\4\3\2X[\5\24\13")
        buf.write("\2Y[\3\2\2\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\31\3\2\2\2")
        buf.write("\t\34&-=CJZ")
        return buf.getvalue()


class pysonParser ( Parser ):

    grammarFileName = "pyson.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'self'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "':'", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "TRUE", "FALSE", "NONE", 
                      "SELF", "KEY", "STRING", "OBJECT", "COLON", "COMMA", 
                      "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", "RIGHT_LIST", 
                      "LEFT_BUKKET", "RIGHT_BUKKEFT", "LINE_COMMENT", "COMMENT", 
                      "WS" ]

    RULE_entry_point = 0
    RULE_item_dict = 1
    RULE_items = 2
    RULE_other_items = 3
    RULE_item = 4
    RULE_value = 5
    RULE_values = 6
    RULE_other_values = 7
    RULE_item_list = 8
    RULE_item_tuple = 9
    RULE_object_name = 10
    RULE_item_object = 11

    ruleNames =  [ "entry_point", "item_dict", "items", "other_items", "item", 
                   "value", "values", "other_values", "item_list", "item_tuple", 
                   "object_name", "item_object" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    TRUE=3
    FALSE=4
    NONE=5
    SELF=6
    KEY=7
    STRING=8
    OBJECT=9
    COLON=10
    COMMA=11
    LEFT_DICT=12
    RIGHT_DICT=13
    LEFT_LIST=14
    RIGHT_LIST=15
    LEFT_BUKKET=16
    RIGHT_BUKKEFT=17
    LINE_COMMENT=18
    COMMENT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Entry_pointContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_dict(self):
            return self.getTypedRuleContext(pysonParser.Item_dictContext,0)


        def item_list(self):
            return self.getTypedRuleContext(pysonParser.Item_listContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_entry_point

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry_point" ):
                listener.enterEntry_point(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry_point" ):
                listener.exitEntry_point(self)




    def entry_point(self):

        localctx = pysonParser.Entry_pointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entry_point)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.LEFT_DICT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.item_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Item_dictContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_DICT(self):
            return self.getToken(pysonParser.LEFT_DICT, 0)

        def items(self):
            return self.getTypedRuleContext(pysonParser.ItemsContext,0)


        def RIGHT_DICT(self):
            return self.getToken(pysonParser.RIGHT_DICT, 0)

        def getRuleIndex(self):
            return pysonParser.RULE_item_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_dict" ):
                listener.enterItem_dict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_dict" ):
                listener.exitItem_dict(self)




    def item_dict(self):

        localctx = pysonParser.Item_dictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_item_dict)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(pysonParser.LEFT_DICT)
            self.state = 29
            self.items()
            self.state = 30
            self.match(pysonParser.RIGHT_DICT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(pysonParser.ItemContext,0)


        def other_items(self):
            return self.getTypedRuleContext(pysonParser.Other_itemsContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)




    def items(self):

        localctx = pysonParser.ItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_items)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.KEY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.item()
                self.state = 33
                self.other_items()
                pass
            elif token in [pysonParser.RIGHT_DICT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Other_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(pysonParser.COLON, 0)

        def item(self):
            return self.getTypedRuleContext(pysonParser.ItemContext,0)


        def other_items(self):
            return self.getTypedRuleContext(pysonParser.Other_itemsContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_other_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_items" ):
                listener.enterOther_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_items" ):
                listener.exitOther_items(self)




    def other_items(self):

        localctx = pysonParser.Other_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_other_items)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(pysonParser.COLON)
                self.state = 39
                self.item()
                self.state = 40
                self.other_items()
                pass
            elif token in [pysonParser.RIGHT_DICT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(pysonParser.KEY, 0)

        def COMMA(self):
            return self.getToken(pysonParser.COMMA, 0)

        def value(self):
            return self.getTypedRuleContext(pysonParser.ValueContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = pysonParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(pysonParser.KEY)
            self.state = 46
            self.match(pysonParser.COMMA)
            self.state = 47
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(pysonParser.INT, 0)

        def FLOAT(self):
            return self.getToken(pysonParser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(pysonParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(pysonParser.FALSE, 0)

        def NONE(self):
            return self.getToken(pysonParser.NONE, 0)

        def STRING(self):
            return self.getToken(pysonParser.STRING, 0)

        def SELF(self):
            return self.getToken(pysonParser.SELF, 0)

        def item_dict(self):
            return self.getTypedRuleContext(pysonParser.Item_dictContext,0)


        def item_list(self):
            return self.getTypedRuleContext(pysonParser.Item_listContext,0)


        def item_object(self):
            return self.getTypedRuleContext(pysonParser.Item_objectContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = pysonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(pysonParser.INT)
                pass
            elif token in [pysonParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(pysonParser.FLOAT)
                pass
            elif token in [pysonParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(pysonParser.TRUE)
                pass
            elif token in [pysonParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(pysonParser.FALSE)
                pass
            elif token in [pysonParser.NONE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(pysonParser.NONE)
                pass
            elif token in [pysonParser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.match(pysonParser.STRING)
                pass
            elif token in [pysonParser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.match(pysonParser.SELF)
                pass
            elif token in [pysonParser.LEFT_DICT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 9)
                self.state = 57
                self.item_list()
                pass
            elif token in [pysonParser.KEY, pysonParser.OBJECT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
                self.item_object()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(pysonParser.ValueContext,0)


        def other_values(self):
            return self.getTypedRuleContext(pysonParser.Other_valuesContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = pysonParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_values)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.INT, pysonParser.FLOAT, pysonParser.TRUE, pysonParser.FALSE, pysonParser.NONE, pysonParser.SELF, pysonParser.KEY, pysonParser.STRING, pysonParser.OBJECT, pysonParser.LEFT_DICT, pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.value()
                self.state = 62
                self.other_values()
                pass
            elif token in [pysonParser.RIGHT_LIST, pysonParser.RIGHT_BUKKEFT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Other_valuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(pysonParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(pysonParser.ValueContext,0)


        def other_values(self):
            return self.getTypedRuleContext(pysonParser.Other_valuesContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_other_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_values" ):
                listener.enterOther_values(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_values" ):
                listener.exitOther_values(self)




    def other_values(self):

        localctx = pysonParser.Other_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_other_values)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(pysonParser.COLON)
                self.state = 68
                self.value()
                self.state = 69
                self.other_values()
                pass
            elif token in [pysonParser.RIGHT_LIST, pysonParser.RIGHT_BUKKEFT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Item_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_LIST(self):
            return self.getToken(pysonParser.LEFT_LIST, 0)

        def values(self):
            return self.getTypedRuleContext(pysonParser.ValuesContext,0)


        def RIGHT_LIST(self):
            return self.getToken(pysonParser.RIGHT_LIST, 0)

        def getRuleIndex(self):
            return pysonParser.RULE_item_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_list" ):
                listener.enterItem_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_list" ):
                listener.exitItem_list(self)




    def item_list(self):

        localctx = pysonParser.Item_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_item_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(pysonParser.LEFT_LIST)
            self.state = 75
            self.values()
            self.state = 76
            self.match(pysonParser.RIGHT_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Item_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BUKKET(self):
            return self.getToken(pysonParser.LEFT_BUKKET, 0)

        def values(self):
            return self.getTypedRuleContext(pysonParser.ValuesContext,0)


        def RIGHT_BUKKEFT(self):
            return self.getToken(pysonParser.RIGHT_BUKKEFT, 0)

        def getRuleIndex(self):
            return pysonParser.RULE_item_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_tuple" ):
                listener.enterItem_tuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_tuple" ):
                listener.exitItem_tuple(self)




    def item_tuple(self):

        localctx = pysonParser.Item_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_item_tuple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(pysonParser.LEFT_BUKKET)
            self.state = 79
            self.values()
            self.state = 80
            self.match(pysonParser.RIGHT_BUKKEFT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Object_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT(self):
            return self.getToken(pysonParser.OBJECT, 0)

        def KEY(self):
            return self.getToken(pysonParser.KEY, 0)

        def getRuleIndex(self):
            return pysonParser.RULE_object_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_name" ):
                listener.enterObject_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_name" ):
                listener.exitObject_name(self)




    def object_name(self):

        localctx = pysonParser.Object_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_object_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==pysonParser.KEY or _la==pysonParser.OBJECT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Item_objectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_name(self):
            return self.getTypedRuleContext(pysonParser.Object_nameContext,0)


        def item_dict(self):
            return self.getTypedRuleContext(pysonParser.Item_dictContext,0)


        def item_tuple(self):
            return self.getTypedRuleContext(pysonParser.Item_tupleContext,0)


        def getRuleIndex(self):
            return pysonParser.RULE_item_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_object" ):
                listener.enterItem_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_object" ):
                listener.exitItem_object(self)




    def item_object(self):

        localctx = pysonParser.Item_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_item_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.object_name()
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.LEFT_DICT]:
                self.state = 85
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_BUKKET]:
                self.state = 86
                self.item_tuple()
                pass
            elif token in [pysonParser.COLON, pysonParser.RIGHT_DICT, pysonParser.RIGHT_LIST, pysonParser.RIGHT_BUKKEFT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





