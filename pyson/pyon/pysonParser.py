# Generated from pyson.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4%\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5,\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7<\n\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("B\n\b\3\t\3\t\3\t\3\t\3\t\5\tI\n\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fW\n\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\2\2]\2\32\3\2\2\2\4\34\3\2\2")
        buf.write("\2\6$\3\2\2\2\b+\3\2\2\2\n-\3\2\2\2\f;\3\2\2\2\16A\3\2")
        buf.write("\2\2\20H\3\2\2\2\22J\3\2\2\2\24N\3\2\2\2\26R\3\2\2\2\30")
        buf.write("\33\5\4\3\2\31\33\5\22\n\2\32\30\3\2\2\2\32\31\3\2\2\2")
        buf.write("\33\3\3\2\2\2\34\35\7\16\2\2\35\36\5\6\4\2\36\37\7\17")
        buf.write("\2\2\37\5\3\2\2\2 !\5\n\6\2!\"\5\b\5\2\"%\3\2\2\2#%\3")
        buf.write("\2\2\2$ \3\2\2\2$#\3\2\2\2%\7\3\2\2\2&\'\7\f\2\2\'(\5")
        buf.write("\n\6\2()\5\b\5\2),\3\2\2\2*,\3\2\2\2+&\3\2\2\2+*\3\2\2")
        buf.write("\2,\t\3\2\2\2-.\7\t\2\2./\7\r\2\2/\60\5\f\7\2\60\13\3")
        buf.write("\2\2\2\61<\7\3\2\2\62<\7\4\2\2\63<\7\5\2\2\64<\7\6\2\2")
        buf.write("\65<\7\7\2\2\66<\7\n\2\2\67<\7\b\2\28<\5\4\3\29<\5\22")
        buf.write("\n\2:<\5\26\f\2;\61\3\2\2\2;\62\3\2\2\2;\63\3\2\2\2;\64")
        buf.write("\3\2\2\2;\65\3\2\2\2;\66\3\2\2\2;\67\3\2\2\2;8\3\2\2\2")
        buf.write(";9\3\2\2\2;:\3\2\2\2<\r\3\2\2\2=>\5\f\7\2>?\5\20\t\2?")
        buf.write("B\3\2\2\2@B\3\2\2\2A=\3\2\2\2A@\3\2\2\2B\17\3\2\2\2CD")
        buf.write("\7\f\2\2DE\5\f\7\2EF\5\20\t\2FI\3\2\2\2GI\3\2\2\2HC\3")
        buf.write("\2\2\2HG\3\2\2\2I\21\3\2\2\2JK\7\20\2\2KL\5\16\b\2LM\7")
        buf.write("\21\2\2M\23\3\2\2\2NO\7\22\2\2OP\5\16\b\2PQ\7\23\2\2Q")
        buf.write("\25\3\2\2\2RV\7\13\2\2SW\5\4\3\2TW\5\24\13\2UW\3\2\2\2")
        buf.write("VS\3\2\2\2VT\3\2\2\2VU\3\2\2\2W\27\3\2\2\2\t\32$+;AHV")
        return buf.getvalue()


class pysonParser ( Parser ):

    grammarFileName = "pyson.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'ctx'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "':'", "'{'", "'}'", "'['", "']'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "TRUE", "FALSE", "NONE", 
                      "CTX", "KEY", "STRING", "OBJECT", "COLON", "COMMA", 
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
    RULE_item_object = 10

    ruleNames =  [ "entry_point", "item_dict", "items", "other_items", "item", 
                   "value", "values", "other_values", "item_list", "item_tuple", 
                   "item_object" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    TRUE=3
    FALSE=4
    NONE=5
    CTX=6
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
        self.checkVersion("4.7.2")
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
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.LEFT_DICT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
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
            self.state = 26
            self.match(pysonParser.LEFT_DICT)
            self.state = 27
            self.items()
            self.state = 28
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.KEY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.item()
                self.state = 31
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(pysonParser.COLON)
                self.state = 37
                self.item()
                self.state = 38
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
            self.state = 43
            self.match(pysonParser.KEY)
            self.state = 44
            self.match(pysonParser.COMMA)
            self.state = 45
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

        def CTX(self):
            return self.getToken(pysonParser.CTX, 0)

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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(pysonParser.INT)
                pass
            elif token in [pysonParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(pysonParser.FLOAT)
                pass
            elif token in [pysonParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(pysonParser.TRUE)
                pass
            elif token in [pysonParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(pysonParser.FALSE)
                pass
            elif token in [pysonParser.NONE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(pysonParser.NONE)
                pass
            elif token in [pysonParser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(pysonParser.STRING)
                pass
            elif token in [pysonParser.CTX]:
                self.enterOuterAlt(localctx, 7)
                self.state = 53
                self.match(pysonParser.CTX)
                pass
            elif token in [pysonParser.LEFT_DICT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 54
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 9)
                self.state = 55
                self.item_list()
                pass
            elif token in [pysonParser.OBJECT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 56
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.INT, pysonParser.FLOAT, pysonParser.TRUE, pysonParser.FALSE, pysonParser.NONE, pysonParser.CTX, pysonParser.STRING, pysonParser.OBJECT, pysonParser.LEFT_DICT, pysonParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.value()
                self.state = 60
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(pysonParser.COLON)
                self.state = 66
                self.value()
                self.state = 67
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
            self.state = 72
            self.match(pysonParser.LEFT_LIST)
            self.state = 73
            self.values()
            self.state = 74
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
            self.state = 76
            self.match(pysonParser.LEFT_BUKKET)
            self.state = 77
            self.values()
            self.state = 78
            self.match(pysonParser.RIGHT_BUKKEFT)
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

        def OBJECT(self):
            return self.getToken(pysonParser.OBJECT, 0)

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
        self.enterRule(localctx, 20, self.RULE_item_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(pysonParser.OBJECT)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pysonParser.LEFT_DICT]:
                self.state = 81
                self.item_dict()
                pass
            elif token in [pysonParser.LEFT_BUKKET]:
                self.state = 82
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





