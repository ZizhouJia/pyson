# Generated from pyonScheme.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\5\7;\n\7\3\b\3\b\3\b\5\b@\n\b")
        buf.write("\3\t\3\t\3\t\3\t\5\tF\n\t\3\n\3\n\3\n\3\n\3\n\5\nM\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13X\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16f\n\16\3\17\3\17\3\17\3\17\3\17\5\17m\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36\2\2\2s\2 \3\2\2\2\4#\3\2\2\2\6+\3\2\2\2\b\62")
        buf.write("\3\2\2\2\n\64\3\2\2\2\f:\3\2\2\2\16<\3\2\2\2\20E\3\2\2")
        buf.write("\2\22L\3\2\2\2\24W\3\2\2\2\26Y\3\2\2\2\30]\3\2\2\2\32")
        buf.write("e\3\2\2\2\34l\3\2\2\2\36n\3\2\2\2 !\7\n\2\2!\"\5\4\3\2")
        buf.write("\"\3\3\2\2\2#$\7\17\2\2$%\5\6\4\2%&\7\20\2\2&\5\3\2\2")
        buf.write("\2\'(\5\n\6\2()\5\b\5\2),\3\2\2\2*,\3\2\2\2+\'\3\2\2\2")
        buf.write("+*\3\2\2\2,\7\3\2\2\2-.\7\f\2\2./\5\n\6\2/\60\5\b\5\2")
        buf.write("\60\63\3\2\2\2\61\63\3\2\2\2\62-\3\2\2\2\62\61\3\2\2\2")
        buf.write("\63\t\3\2\2\2\64\65\7\b\2\2\65\66\7\r\2\2\66\67\5\f\7")
        buf.write("\2\67\13\3\2\2\28;\5\4\3\29;\5\16\b\2:8\3\2\2\2:9\3\2")
        buf.write("\2\2;\r\3\2\2\2<?\7\13\2\2=@\5\30\r\2>@\3\2\2\2?=\3\2")
        buf.write("\2\2?>\3\2\2\2@\17\3\2\2\2AB\5\24\13\2BC\5\22\n\2CF\3")
        buf.write("\2\2\2DF\3\2\2\2EA\3\2\2\2ED\3\2\2\2F\21\3\2\2\2GH\7\f")
        buf.write("\2\2HI\5\24\13\2IJ\5\22\n\2JM\3\2\2\2KM\3\2\2\2LG\3\2")
        buf.write("\2\2LK\3\2\2\2M\23\3\2\2\2NX\7\3\2\2OX\7\4\2\2PX\7\5\2")
        buf.write("\2QX\7\6\2\2RX\7\7\2\2SX\7\t\2\2TX\7\n\2\2UX\5\16\b\2")
        buf.write("VX\5\26\f\2WN\3\2\2\2WO\3\2\2\2WP\3\2\2\2WQ\3\2\2\2WR")
        buf.write("\3\2\2\2WS\3\2\2\2WT\3\2\2\2WU\3\2\2\2WV\3\2\2\2X\25\3")
        buf.write("\2\2\2YZ\7\21\2\2Z[\5\20\t\2[\\\7\22\2\2\\\27\3\2\2\2")
        buf.write("]^\7\17\2\2^_\5\32\16\2_`\7\20\2\2`\31\3\2\2\2ab\5\36")
        buf.write("\20\2bc\5\34\17\2cf\3\2\2\2df\3\2\2\2ea\3\2\2\2ed\3\2")
        buf.write("\2\2f\33\3\2\2\2gh\7\f\2\2hi\5\36\20\2ij\5\34\17\2jm\3")
        buf.write("\2\2\2km\3\2\2\2lg\3\2\2\2lk\3\2\2\2m\35\3\2\2\2no\7\b")
        buf.write("\2\2op\7\r\2\2pq\5\24\13\2q\37\3\2\2\2\13+\62:?ELWel")
        return buf.getvalue()


class pyonSchemeParser ( Parser ):

    grammarFileName = "pyonScheme.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "':'", "'.'", "'{'", 
                     "'}'", "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "TRUE", "FALSE", "NONE", 
                      "KEY", "STRING", "OBJECT", "CHECKER", "COLON", "COMMA", 
                      "DOT", "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", "RIGHT_LIST", 
                      "LEFT_BUKKET", "RIGHT_BUKKET", "LINE_COMMENT", "COMMENT", 
                      "WS" ]

    RULE_entry_point = 0
    RULE_checker_dict = 1
    RULE_items = 2
    RULE_other_items = 3
    RULE_item = 4
    RULE_value = 5
    RULE_checker_object = 6
    RULE_list_items = 7
    RULE_other_variable_items = 8
    RULE_variable_item = 9
    RULE_variable_list = 10
    RULE_variable_dict = 11
    RULE_variable_dict_items = 12
    RULE_other_variable_dict_items = 13
    RULE_variable_dict_item = 14

    ruleNames =  [ "entry_point", "checker_dict", "items", "other_items", 
                   "item", "value", "checker_object", "list_items", "other_variable_items", 
                   "variable_item", "variable_list", "variable_dict", "variable_dict_items", 
                   "other_variable_dict_items", "variable_dict_item" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    TRUE=3
    FALSE=4
    NONE=5
    KEY=6
    STRING=7
    OBJECT=8
    CHECKER=9
    COLON=10
    COMMA=11
    DOT=12
    LEFT_DICT=13
    RIGHT_DICT=14
    LEFT_LIST=15
    RIGHT_LIST=16
    LEFT_BUKKET=17
    RIGHT_BUKKET=18
    LINE_COMMENT=19
    COMMENT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Entry_pointContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT(self):
            return self.getToken(pyonSchemeParser.OBJECT, 0)

        def checker_dict(self):
            return self.getTypedRuleContext(pyonSchemeParser.Checker_dictContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_entry_point

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry_point" ):
                listener.enterEntry_point(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry_point" ):
                listener.exitEntry_point(self)




    def entry_point(self):

        localctx = pyonSchemeParser.Entry_pointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entry_point)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(pyonSchemeParser.OBJECT)
            self.state = 31
            self.checker_dict()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Checker_dictContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_DICT(self):
            return self.getToken(pyonSchemeParser.LEFT_DICT, 0)

        def items(self):
            return self.getTypedRuleContext(pyonSchemeParser.ItemsContext,0)


        def RIGHT_DICT(self):
            return self.getToken(pyonSchemeParser.RIGHT_DICT, 0)

        def getRuleIndex(self):
            return pyonSchemeParser.RULE_checker_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChecker_dict" ):
                listener.enterChecker_dict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChecker_dict" ):
                listener.exitChecker_dict(self)




    def checker_dict(self):

        localctx = pyonSchemeParser.Checker_dictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_checker_dict)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(pyonSchemeParser.LEFT_DICT)
            self.state = 34
            self.items()
            self.state = 35
            self.match(pyonSchemeParser.RIGHT_DICT)
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
            return self.getTypedRuleContext(pyonSchemeParser.ItemContext,0)


        def other_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)




    def items(self):

        localctx = pyonSchemeParser.ItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_items)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.KEY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.item()
                self.state = 38
                self.other_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_DICT]:
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
            return self.getToken(pyonSchemeParser.COLON, 0)

        def item(self):
            return self.getTypedRuleContext(pyonSchemeParser.ItemContext,0)


        def other_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_other_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_items" ):
                listener.enterOther_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_items" ):
                listener.exitOther_items(self)




    def other_items(self):

        localctx = pyonSchemeParser.Other_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_other_items)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(pyonSchemeParser.COLON)
                self.state = 44
                self.item()
                self.state = 45
                self.other_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_DICT]:
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
            return self.getToken(pyonSchemeParser.KEY, 0)

        def COMMA(self):
            return self.getToken(pyonSchemeParser.COMMA, 0)

        def value(self):
            return self.getTypedRuleContext(pyonSchemeParser.ValueContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = pyonSchemeParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(pyonSchemeParser.KEY)
            self.state = 51
            self.match(pyonSchemeParser.COMMA)
            self.state = 52
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

        def checker_dict(self):
            return self.getTypedRuleContext(pyonSchemeParser.Checker_dictContext,0)


        def checker_object(self):
            return self.getTypedRuleContext(pyonSchemeParser.Checker_objectContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = pyonSchemeParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.LEFT_DICT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.checker_dict()
                pass
            elif token in [pyonSchemeParser.CHECKER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.checker_object()
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


    class Checker_objectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHECKER(self):
            return self.getToken(pyonSchemeParser.CHECKER, 0)

        def variable_dict(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_dictContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_checker_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChecker_object" ):
                listener.enterChecker_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChecker_object" ):
                listener.exitChecker_object(self)




    def checker_object(self):

        localctx = pyonSchemeParser.Checker_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_checker_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(pyonSchemeParser.CHECKER)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.LEFT_DICT]:
                self.state = 59
                self.variable_dict()
                pass
            elif token in [pyonSchemeParser.COLON, pyonSchemeParser.RIGHT_DICT, pyonSchemeParser.RIGHT_LIST]:
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


    class List_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_item(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_itemContext,0)


        def other_variable_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_variable_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_list_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_items" ):
                listener.enterList_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_items" ):
                listener.exitList_items(self)




    def list_items(self):

        localctx = pyonSchemeParser.List_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_items)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.INT, pyonSchemeParser.FLOAT, pyonSchemeParser.TRUE, pyonSchemeParser.FALSE, pyonSchemeParser.NONE, pyonSchemeParser.STRING, pyonSchemeParser.OBJECT, pyonSchemeParser.CHECKER, pyonSchemeParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.variable_item()
                self.state = 64
                self.other_variable_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_LIST]:
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


    class Other_variable_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(pyonSchemeParser.COLON, 0)

        def variable_item(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_itemContext,0)


        def other_variable_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_variable_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_other_variable_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_variable_items" ):
                listener.enterOther_variable_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_variable_items" ):
                listener.exitOther_variable_items(self)




    def other_variable_items(self):

        localctx = pyonSchemeParser.Other_variable_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_other_variable_items)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(pyonSchemeParser.COLON)
                self.state = 70
                self.variable_item()
                self.state = 71
                self.other_variable_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_LIST]:
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


    class Variable_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(pyonSchemeParser.INT, 0)

        def FLOAT(self):
            return self.getToken(pyonSchemeParser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(pyonSchemeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(pyonSchemeParser.FALSE, 0)

        def NONE(self):
            return self.getToken(pyonSchemeParser.NONE, 0)

        def STRING(self):
            return self.getToken(pyonSchemeParser.STRING, 0)

        def OBJECT(self):
            return self.getToken(pyonSchemeParser.OBJECT, 0)

        def checker_object(self):
            return self.getTypedRuleContext(pyonSchemeParser.Checker_objectContext,0)


        def variable_list(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_listContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_variable_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_item" ):
                listener.enterVariable_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_item" ):
                listener.exitVariable_item(self)




    def variable_item(self):

        localctx = pyonSchemeParser.Variable_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variable_item)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(pyonSchemeParser.INT)
                pass
            elif token in [pyonSchemeParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(pyonSchemeParser.FLOAT)
                pass
            elif token in [pyonSchemeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(pyonSchemeParser.TRUE)
                pass
            elif token in [pyonSchemeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(pyonSchemeParser.FALSE)
                pass
            elif token in [pyonSchemeParser.NONE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(pyonSchemeParser.NONE)
                pass
            elif token in [pyonSchemeParser.STRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.match(pyonSchemeParser.STRING)
                pass
            elif token in [pyonSchemeParser.OBJECT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.match(pyonSchemeParser.OBJECT)
                pass
            elif token in [pyonSchemeParser.CHECKER]:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.checker_object()
                pass
            elif token in [pyonSchemeParser.LEFT_LIST]:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.variable_list()
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


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_LIST(self):
            return self.getToken(pyonSchemeParser.LEFT_LIST, 0)

        def list_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.List_itemsContext,0)


        def RIGHT_LIST(self):
            return self.getToken(pyonSchemeParser.RIGHT_LIST, 0)

        def getRuleIndex(self):
            return pyonSchemeParser.RULE_variable_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_list" ):
                listener.enterVariable_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_list" ):
                listener.exitVariable_list(self)




    def variable_list(self):

        localctx = pyonSchemeParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(pyonSchemeParser.LEFT_LIST)
            self.state = 88
            self.list_items()
            self.state = 89
            self.match(pyonSchemeParser.RIGHT_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_dictContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_DICT(self):
            return self.getToken(pyonSchemeParser.LEFT_DICT, 0)

        def variable_dict_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_dict_itemsContext,0)


        def RIGHT_DICT(self):
            return self.getToken(pyonSchemeParser.RIGHT_DICT, 0)

        def getRuleIndex(self):
            return pyonSchemeParser.RULE_variable_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_dict" ):
                listener.enterVariable_dict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_dict" ):
                listener.exitVariable_dict(self)




    def variable_dict(self):

        localctx = pyonSchemeParser.Variable_dictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variable_dict)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(pyonSchemeParser.LEFT_DICT)
            self.state = 92
            self.variable_dict_items()
            self.state = 93
            self.match(pyonSchemeParser.RIGHT_DICT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_dict_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_dict_item(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_dict_itemContext,0)


        def other_variable_dict_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_variable_dict_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_variable_dict_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_dict_items" ):
                listener.enterVariable_dict_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_dict_items" ):
                listener.exitVariable_dict_items(self)




    def variable_dict_items(self):

        localctx = pyonSchemeParser.Variable_dict_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable_dict_items)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.KEY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.variable_dict_item()
                self.state = 96
                self.other_variable_dict_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_DICT]:
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


    class Other_variable_dict_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(pyonSchemeParser.COLON, 0)

        def variable_dict_item(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_dict_itemContext,0)


        def other_variable_dict_items(self):
            return self.getTypedRuleContext(pyonSchemeParser.Other_variable_dict_itemsContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_other_variable_dict_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_variable_dict_items" ):
                listener.enterOther_variable_dict_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_variable_dict_items" ):
                listener.exitOther_variable_dict_items(self)




    def other_variable_dict_items(self):

        localctx = pyonSchemeParser.Other_variable_dict_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_other_variable_dict_items)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyonSchemeParser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(pyonSchemeParser.COLON)
                self.state = 102
                self.variable_dict_item()
                self.state = 103
                self.other_variable_dict_items()
                pass
            elif token in [pyonSchemeParser.RIGHT_DICT]:
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


    class Variable_dict_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(pyonSchemeParser.KEY, 0)

        def COMMA(self):
            return self.getToken(pyonSchemeParser.COMMA, 0)

        def variable_item(self):
            return self.getTypedRuleContext(pyonSchemeParser.Variable_itemContext,0)


        def getRuleIndex(self):
            return pyonSchemeParser.RULE_variable_dict_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_dict_item" ):
                listener.enterVariable_dict_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_dict_item" ):
                listener.exitVariable_dict_item(self)




    def variable_dict_item(self):

        localctx = pyonSchemeParser.Variable_dict_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable_dict_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(pyonSchemeParser.KEY)
            self.state = 109
            self.match(pyonSchemeParser.COMMA)
            self.state = 110
            self.variable_item()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





