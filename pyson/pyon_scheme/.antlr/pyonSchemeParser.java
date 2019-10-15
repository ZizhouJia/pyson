// Generated from /home/jiazizhou/antlr/pyon_scheme/pyonScheme.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyonSchemeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, KEY=6, STRING=7, OBJECT=8, CHECKER=9, 
		COLON=10, COMMA=11, DOT=12, LEFT_DICT=13, RIGHT_DICT=14, LEFT_LIST=15, 
		RIGHT_LIST=16, LEFT_BUKKET=17, RIGHT_BUKKET=18, LINE_COMMENT=19, COMMENT=20, 
		WS=21;
	public static final int
		RULE_entry_point = 0, RULE_checker_dict = 1, RULE_items = 2, RULE_other_items = 3, 
		RULE_item = 4, RULE_value = 5, RULE_checker_object = 6, RULE_list_items = 7, 
		RULE_other_variable_items = 8, RULE_variable_item = 9, RULE_variable_list = 10, 
		RULE_variable_dict = 11, RULE_variable_dict_items = 12, RULE_other_variable_dict_items = 13, 
		RULE_variable_dict_item = 14;
	public static final String[] ruleNames = {
		"entry_point", "checker_dict", "items", "other_items", "item", "value", 
		"checker_object", "list_items", "other_variable_items", "variable_item", 
		"variable_list", "variable_dict", "variable_dict_items", "other_variable_dict_items", 
		"variable_dict_item"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, null, null, null, null, "','", "':'", 
		"'.'", "'{'", "'}'", "'['", "']'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "INT", "FLOAT", "TRUE", "FALSE", "NONE", "KEY", "STRING", "OBJECT", 
		"CHECKER", "COLON", "COMMA", "DOT", "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", 
		"RIGHT_LIST", "LEFT_BUKKET", "RIGHT_BUKKET", "LINE_COMMENT", "COMMENT", 
		"WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "pyonScheme.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pyonSchemeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class Entry_pointContext extends ParserRuleContext {
		public TerminalNode OBJECT() { return getToken(pyonSchemeParser.OBJECT, 0); }
		public Checker_dictContext checker_dict() {
			return getRuleContext(Checker_dictContext.class,0);
		}
		public Entry_pointContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entry_point; }
	}

	public final Entry_pointContext entry_point() throws RecognitionException {
		Entry_pointContext _localctx = new Entry_pointContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_entry_point);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(OBJECT);
			setState(31);
			checker_dict();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Checker_dictContext extends ParserRuleContext {
		public TerminalNode LEFT_DICT() { return getToken(pyonSchemeParser.LEFT_DICT, 0); }
		public ItemsContext items() {
			return getRuleContext(ItemsContext.class,0);
		}
		public TerminalNode RIGHT_DICT() { return getToken(pyonSchemeParser.RIGHT_DICT, 0); }
		public Checker_dictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_checker_dict; }
	}

	public final Checker_dictContext checker_dict() throws RecognitionException {
		Checker_dictContext _localctx = new Checker_dictContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_checker_dict);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(LEFT_DICT);
			setState(34);
			items();
			setState(35);
			match(RIGHT_DICT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemsContext extends ParserRuleContext {
		public ItemContext item() {
			return getRuleContext(ItemContext.class,0);
		}
		public Other_itemsContext other_items() {
			return getRuleContext(Other_itemsContext.class,0);
		}
		public ItemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_items; }
	}

	public final ItemsContext items() throws RecognitionException {
		ItemsContext _localctx = new ItemsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_items);
		try {
			setState(41);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				item();
				setState(38);
				other_items();
				}
				break;
			case RIGHT_DICT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Other_itemsContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(pyonSchemeParser.COLON, 0); }
		public ItemContext item() {
			return getRuleContext(ItemContext.class,0);
		}
		public Other_itemsContext other_items() {
			return getRuleContext(Other_itemsContext.class,0);
		}
		public Other_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other_items; }
	}

	public final Other_itemsContext other_items() throws RecognitionException {
		Other_itemsContext _localctx = new Other_itemsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_other_items);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(43);
				match(COLON);
				setState(44);
				item();
				setState(45);
				other_items();
				}
				break;
			case RIGHT_DICT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemContext extends ParserRuleContext {
		public TerminalNode KEY() { return getToken(pyonSchemeParser.KEY, 0); }
		public TerminalNode COMMA() { return getToken(pyonSchemeParser.COMMA, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_item);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(KEY);
			setState(51);
			match(COMMA);
			setState(52);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public Checker_dictContext checker_dict() {
			return getRuleContext(Checker_dictContext.class,0);
		}
		public Checker_objectContext checker_object() {
			return getRuleContext(Checker_objectContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_value);
		try {
			setState(56);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_DICT:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				checker_dict();
				}
				break;
			case CHECKER:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				checker_object();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Checker_objectContext extends ParserRuleContext {
		public TerminalNode CHECKER() { return getToken(pyonSchemeParser.CHECKER, 0); }
		public Variable_dictContext variable_dict() {
			return getRuleContext(Variable_dictContext.class,0);
		}
		public Checker_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_checker_object; }
	}

	public final Checker_objectContext checker_object() throws RecognitionException {
		Checker_objectContext _localctx = new Checker_objectContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_checker_object);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(CHECKER);
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_DICT:
				{
				setState(59);
				variable_dict();
				}
				break;
			case COLON:
			case RIGHT_DICT:
			case RIGHT_LIST:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class List_itemsContext extends ParserRuleContext {
		public Variable_itemContext variable_item() {
			return getRuleContext(Variable_itemContext.class,0);
		}
		public Other_variable_itemsContext other_variable_items() {
			return getRuleContext(Other_variable_itemsContext.class,0);
		}
		public List_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_items; }
	}

	public final List_itemsContext list_items() throws RecognitionException {
		List_itemsContext _localctx = new List_itemsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_list_items);
		try {
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case TRUE:
			case FALSE:
			case NONE:
			case STRING:
			case OBJECT:
			case CHECKER:
			case LEFT_LIST:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				variable_item();
				setState(64);
				other_variable_items();
				}
				break;
			case RIGHT_LIST:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Other_variable_itemsContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(pyonSchemeParser.COLON, 0); }
		public Variable_itemContext variable_item() {
			return getRuleContext(Variable_itemContext.class,0);
		}
		public Other_variable_itemsContext other_variable_items() {
			return getRuleContext(Other_variable_itemsContext.class,0);
		}
		public Other_variable_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other_variable_items; }
	}

	public final Other_variable_itemsContext other_variable_items() throws RecognitionException {
		Other_variable_itemsContext _localctx = new Other_variable_itemsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_other_variable_items);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(COLON);
				setState(70);
				variable_item();
				setState(71);
				other_variable_items();
				}
				break;
			case RIGHT_LIST:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_itemContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(pyonSchemeParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(pyonSchemeParser.FLOAT, 0); }
		public TerminalNode TRUE() { return getToken(pyonSchemeParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(pyonSchemeParser.FALSE, 0); }
		public TerminalNode NONE() { return getToken(pyonSchemeParser.NONE, 0); }
		public TerminalNode STRING() { return getToken(pyonSchemeParser.STRING, 0); }
		public TerminalNode OBJECT() { return getToken(pyonSchemeParser.OBJECT, 0); }
		public Checker_objectContext checker_object() {
			return getRuleContext(Checker_objectContext.class,0);
		}
		public Variable_listContext variable_list() {
			return getRuleContext(Variable_listContext.class,0);
		}
		public Variable_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_item; }
	}

	public final Variable_itemContext variable_item() throws RecognitionException {
		Variable_itemContext _localctx = new Variable_itemContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_variable_item);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				match(FLOAT);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 3);
				{
				setState(78);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(79);
				match(FALSE);
				}
				break;
			case NONE:
				enterOuterAlt(_localctx, 5);
				{
				setState(80);
				match(NONE);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 6);
				{
				setState(81);
				match(STRING);
				}
				break;
			case OBJECT:
				enterOuterAlt(_localctx, 7);
				{
				setState(82);
				match(OBJECT);
				}
				break;
			case CHECKER:
				enterOuterAlt(_localctx, 8);
				{
				setState(83);
				checker_object();
				}
				break;
			case LEFT_LIST:
				enterOuterAlt(_localctx, 9);
				{
				setState(84);
				variable_list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_listContext extends ParserRuleContext {
		public TerminalNode LEFT_LIST() { return getToken(pyonSchemeParser.LEFT_LIST, 0); }
		public List_itemsContext list_items() {
			return getRuleContext(List_itemsContext.class,0);
		}
		public TerminalNode RIGHT_LIST() { return getToken(pyonSchemeParser.RIGHT_LIST, 0); }
		public Variable_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_list; }
	}

	public final Variable_listContext variable_list() throws RecognitionException {
		Variable_listContext _localctx = new Variable_listContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variable_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(LEFT_LIST);
			setState(88);
			list_items();
			setState(89);
			match(RIGHT_LIST);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_dictContext extends ParserRuleContext {
		public TerminalNode LEFT_DICT() { return getToken(pyonSchemeParser.LEFT_DICT, 0); }
		public Variable_dict_itemsContext variable_dict_items() {
			return getRuleContext(Variable_dict_itemsContext.class,0);
		}
		public TerminalNode RIGHT_DICT() { return getToken(pyonSchemeParser.RIGHT_DICT, 0); }
		public Variable_dictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_dict; }
	}

	public final Variable_dictContext variable_dict() throws RecognitionException {
		Variable_dictContext _localctx = new Variable_dictContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_variable_dict);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(LEFT_DICT);
			setState(92);
			variable_dict_items();
			setState(93);
			match(RIGHT_DICT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_dict_itemsContext extends ParserRuleContext {
		public Variable_dict_itemContext variable_dict_item() {
			return getRuleContext(Variable_dict_itemContext.class,0);
		}
		public Other_variable_dict_itemsContext other_variable_dict_items() {
			return getRuleContext(Other_variable_dict_itemsContext.class,0);
		}
		public Variable_dict_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_dict_items; }
	}

	public final Variable_dict_itemsContext variable_dict_items() throws RecognitionException {
		Variable_dict_itemsContext _localctx = new Variable_dict_itemsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_variable_dict_items);
		try {
			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				variable_dict_item();
				setState(96);
				other_variable_dict_items();
				}
				break;
			case RIGHT_DICT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Other_variable_dict_itemsContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(pyonSchemeParser.COLON, 0); }
		public Variable_dict_itemContext variable_dict_item() {
			return getRuleContext(Variable_dict_itemContext.class,0);
		}
		public Other_variable_dict_itemsContext other_variable_dict_items() {
			return getRuleContext(Other_variable_dict_itemsContext.class,0);
		}
		public Other_variable_dict_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other_variable_dict_items; }
	}

	public final Other_variable_dict_itemsContext other_variable_dict_items() throws RecognitionException {
		Other_variable_dict_itemsContext _localctx = new Other_variable_dict_itemsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_other_variable_dict_items);
		try {
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				match(COLON);
				setState(102);
				variable_dict_item();
				setState(103);
				other_variable_dict_items();
				}
				break;
			case RIGHT_DICT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_dict_itemContext extends ParserRuleContext {
		public TerminalNode KEY() { return getToken(pyonSchemeParser.KEY, 0); }
		public TerminalNode COMMA() { return getToken(pyonSchemeParser.COMMA, 0); }
		public Variable_itemContext variable_item() {
			return getRuleContext(Variable_itemContext.class,0);
		}
		public Variable_dict_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_dict_item; }
	}

	public final Variable_dict_itemContext variable_dict_item() throws RecognitionException {
		Variable_dict_itemContext _localctx = new Variable_dict_itemContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_variable_dict_item);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(KEY);
			setState(109);
			match(COMMA);
			setState(110);
			variable_item();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27s\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\3\3"+
		"\3\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\5\7;\n\7\3\b\3\b\3\b\5\b@\n\b\3\t\3\t\3\t\3\t\5\tF\n\t\3"+
		"\n\3\n\3\n\3\n\3\n\5\nM\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\5\13X\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16"+
		"f\n\16\3\17\3\17\3\17\3\17\3\17\5\17m\n\17\3\20\3\20\3\20\3\20\3\20\2"+
		"\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\2\2s\2 \3\2\2\2\4#\3\2"+
		"\2\2\6+\3\2\2\2\b\62\3\2\2\2\n\64\3\2\2\2\f:\3\2\2\2\16<\3\2\2\2\20E\3"+
		"\2\2\2\22L\3\2\2\2\24W\3\2\2\2\26Y\3\2\2\2\30]\3\2\2\2\32e\3\2\2\2\34"+
		"l\3\2\2\2\36n\3\2\2\2 !\7\n\2\2!\"\5\4\3\2\"\3\3\2\2\2#$\7\17\2\2$%\5"+
		"\6\4\2%&\7\20\2\2&\5\3\2\2\2\'(\5\n\6\2()\5\b\5\2),\3\2\2\2*,\3\2\2\2"+
		"+\'\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-.\7\f\2\2./\5\n\6\2/\60\5\b\5\2\60\63"+
		"\3\2\2\2\61\63\3\2\2\2\62-\3\2\2\2\62\61\3\2\2\2\63\t\3\2\2\2\64\65\7"+
		"\b\2\2\65\66\7\r\2\2\66\67\5\f\7\2\67\13\3\2\2\28;\5\4\3\29;\5\16\b\2"+
		":8\3\2\2\2:9\3\2\2\2;\r\3\2\2\2<?\7\13\2\2=@\5\30\r\2>@\3\2\2\2?=\3\2"+
		"\2\2?>\3\2\2\2@\17\3\2\2\2AB\5\24\13\2BC\5\22\n\2CF\3\2\2\2DF\3\2\2\2"+
		"EA\3\2\2\2ED\3\2\2\2F\21\3\2\2\2GH\7\f\2\2HI\5\24\13\2IJ\5\22\n\2JM\3"+
		"\2\2\2KM\3\2\2\2LG\3\2\2\2LK\3\2\2\2M\23\3\2\2\2NX\7\3\2\2OX\7\4\2\2P"+
		"X\7\5\2\2QX\7\6\2\2RX\7\7\2\2SX\7\t\2\2TX\7\n\2\2UX\5\16\b\2VX\5\26\f"+
		"\2WN\3\2\2\2WO\3\2\2\2WP\3\2\2\2WQ\3\2\2\2WR\3\2\2\2WS\3\2\2\2WT\3\2\2"+
		"\2WU\3\2\2\2WV\3\2\2\2X\25\3\2\2\2YZ\7\21\2\2Z[\5\20\t\2[\\\7\22\2\2\\"+
		"\27\3\2\2\2]^\7\17\2\2^_\5\32\16\2_`\7\20\2\2`\31\3\2\2\2ab\5\36\20\2"+
		"bc\5\34\17\2cf\3\2\2\2df\3\2\2\2ea\3\2\2\2ed\3\2\2\2f\33\3\2\2\2gh\7\f"+
		"\2\2hi\5\36\20\2ij\5\34\17\2jm\3\2\2\2km\3\2\2\2lg\3\2\2\2lk\3\2\2\2m"+
		"\35\3\2\2\2no\7\b\2\2op\7\r\2\2pq\5\24\13\2q\37\3\2\2\2\13+\62:?ELWel";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}