// Generated from /home/jiazizhou/antlr/pyon_scheme/pyon_scheme.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyon_schemeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, KEY=6, STRING=7, OBJECT=8, COLON=9, 
		COMMA=10, DOT=11, LEFT_DICT=12, RIGHT_DICT=13, LEFT_LIST=14, RIGHT_LIST=15, 
		LEFT_BUKKET=16, RIGHT_BUKKET=17, LINE_COMMENT=18, COMMENT=19, WS=20;
	public static final int
		RULE_entry_point = 0, RULE_item_dict = 1, RULE_items = 2, RULE_other_items = 3, 
		RULE_item = 4, RULE_value = 5, RULE_item_object = 6, RULE_variable_tuple = 7, 
		RULE_variable_tuple_items = 8, RULE_other_variable_items = 9, RULE_variable_item = 10, 
		RULE_variable_list = 11, RULE_variable_object = 12, RULE_variable_dict = 13, 
		RULE_variable_dict_items = 14, RULE_other_variable_dict_items = 15, RULE_variable_dict_item = 16;
	public static final String[] ruleNames = {
		"entry_point", "item_dict", "items", "other_items", "item", "value", "item_object", 
		"variable_tuple", "variable_tuple_items", "other_variable_items", "variable_item", 
		"variable_list", "variable_object", "variable_dict", "variable_dict_items", 
		"other_variable_dict_items", "variable_dict_item"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, null, null, null, "','", "':'", "'.'", 
		"'{'", "'}'", "'['", "']'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "INT", "FLOAT", "TRUE", "FALSE", "NONE", "KEY", "STRING", "OBJECT", 
		"COLON", "COMMA", "DOT", "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", "RIGHT_LIST", 
		"LEFT_BUKKET", "RIGHT_BUKKET", "LINE_COMMENT", "COMMENT", "WS"
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
	public String getGrammarFileName() { return "pyon_scheme.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pyon_schemeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class Entry_pointContext extends ParserRuleContext {
		public Item_dictContext item_dict() {
			return getRuleContext(Item_dictContext.class,0);
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
			setState(34);
			item_dict();
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

	public static class Item_dictContext extends ParserRuleContext {
		public TerminalNode LEFT_DICT() { return getToken(pyon_schemeParser.LEFT_DICT, 0); }
		public ItemsContext items() {
			return getRuleContext(ItemsContext.class,0);
		}
		public TerminalNode RIGHT_DICT() { return getToken(pyon_schemeParser.RIGHT_DICT, 0); }
		public Item_dictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_dict; }
	}

	public final Item_dictContext item_dict() throws RecognitionException {
		Item_dictContext _localctx = new Item_dictContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_item_dict);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(LEFT_DICT);
			setState(37);
			items();
			setState(38);
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
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				item();
				setState(41);
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
		public TerminalNode COLON() { return getToken(pyon_schemeParser.COLON, 0); }
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
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				match(COLON);
				setState(47);
				item();
				setState(48);
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
		public TerminalNode KEY() { return getToken(pyon_schemeParser.KEY, 0); }
		public TerminalNode COMMA() { return getToken(pyon_schemeParser.COMMA, 0); }
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
			setState(53);
			match(KEY);
			setState(54);
			match(COMMA);
			setState(55);
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
		public Item_dictContext item_dict() {
			return getRuleContext(Item_dictContext.class,0);
		}
		public Item_objectContext item_object() {
			return getRuleContext(Item_objectContext.class,0);
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
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_DICT:
				enterOuterAlt(_localctx, 1);
				{
				setState(57);
				item_dict();
				}
				break;
			case OBJECT:
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				item_object();
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

	public static class Item_objectContext extends ParserRuleContext {
		public TerminalNode OBJECT() { return getToken(pyon_schemeParser.OBJECT, 0); }
		public Variable_tupleContext variable_tuple() {
			return getRuleContext(Variable_tupleContext.class,0);
		}
		public Variable_dictContext variable_dict() {
			return getRuleContext(Variable_dictContext.class,0);
		}
		public Item_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_object; }
	}

	public final Item_objectContext item_object() throws RecognitionException {
		Item_objectContext _localctx = new Item_objectContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_item_object);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(OBJECT);
			setState(64);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_BUKKET:
				{
				setState(62);
				variable_tuple();
				}
				break;
			case LEFT_DICT:
				{
				setState(63);
				variable_dict();
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

	public static class Variable_tupleContext extends ParserRuleContext {
		public TerminalNode LEFT_BUKKET() { return getToken(pyon_schemeParser.LEFT_BUKKET, 0); }
		public Variable_tuple_itemsContext variable_tuple_items() {
			return getRuleContext(Variable_tuple_itemsContext.class,0);
		}
		public TerminalNode RIGHT_BUKKET() { return getToken(pyon_schemeParser.RIGHT_BUKKET, 0); }
		public Variable_tupleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_tuple; }
	}

	public final Variable_tupleContext variable_tuple() throws RecognitionException {
		Variable_tupleContext _localctx = new Variable_tupleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_variable_tuple);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(LEFT_BUKKET);
			setState(67);
			variable_tuple_items();
			setState(68);
			match(RIGHT_BUKKET);
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

	public static class Variable_tuple_itemsContext extends ParserRuleContext {
		public Variable_itemContext variable_item() {
			return getRuleContext(Variable_itemContext.class,0);
		}
		public Other_variable_itemsContext other_variable_items() {
			return getRuleContext(Other_variable_itemsContext.class,0);
		}
		public Variable_tuple_itemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_tuple_items; }
	}

	public final Variable_tuple_itemsContext variable_tuple_items() throws RecognitionException {
		Variable_tuple_itemsContext _localctx = new Variable_tuple_itemsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_variable_tuple_items);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case TRUE:
			case FALSE:
			case NONE:
			case OBJECT:
			case LEFT_LIST:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				variable_item();
				setState(71);
				other_variable_items();
				}
				break;
			case RIGHT_LIST:
			case RIGHT_BUKKET:
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
		public TerminalNode COLON() { return getToken(pyon_schemeParser.COLON, 0); }
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
		enterRule(_localctx, 18, RULE_other_variable_items);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				match(COLON);
				setState(77);
				variable_item();
				setState(78);
				other_variable_items();
				}
				break;
			case RIGHT_LIST:
			case RIGHT_BUKKET:
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
		public TerminalNode INT() { return getToken(pyon_schemeParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(pyon_schemeParser.FLOAT, 0); }
		public TerminalNode TRUE() { return getToken(pyon_schemeParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(pyon_schemeParser.FALSE, 0); }
		public TerminalNode NONE() { return getToken(pyon_schemeParser.NONE, 0); }
		public Variable_listContext variable_list() {
			return getRuleContext(Variable_listContext.class,0);
		}
		public Variable_objectContext variable_object() {
			return getRuleContext(Variable_objectContext.class,0);
		}
		public Variable_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_item; }
	}

	public final Variable_itemContext variable_item() throws RecognitionException {
		Variable_itemContext _localctx = new Variable_itemContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variable_item);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				match(FLOAT);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 3);
				{
				setState(85);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(86);
				match(FALSE);
				}
				break;
			case NONE:
				enterOuterAlt(_localctx, 5);
				{
				setState(87);
				match(NONE);
				}
				break;
			case LEFT_LIST:
				enterOuterAlt(_localctx, 6);
				{
				setState(88);
				variable_list();
				}
				break;
			case OBJECT:
				enterOuterAlt(_localctx, 7);
				{
				setState(89);
				variable_object();
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
		public TerminalNode LEFT_LIST() { return getToken(pyon_schemeParser.LEFT_LIST, 0); }
		public Variable_tuple_itemsContext variable_tuple_items() {
			return getRuleContext(Variable_tuple_itemsContext.class,0);
		}
		public TerminalNode RIGHT_LIST() { return getToken(pyon_schemeParser.RIGHT_LIST, 0); }
		public Variable_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_list; }
	}

	public final Variable_listContext variable_list() throws RecognitionException {
		Variable_listContext _localctx = new Variable_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_variable_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(LEFT_LIST);
			setState(93);
			variable_tuple_items();
			setState(94);
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

	public static class Variable_objectContext extends ParserRuleContext {
		public TerminalNode OBJECT() { return getToken(pyon_schemeParser.OBJECT, 0); }
		public TerminalNode LEFT_DICT() { return getToken(pyon_schemeParser.LEFT_DICT, 0); }
		public TerminalNode RIGHT_DICT() { return getToken(pyon_schemeParser.RIGHT_DICT, 0); }
		public TerminalNode DOT() { return getToken(pyon_schemeParser.DOT, 0); }
		public ItemsContext items() {
			return getRuleContext(ItemsContext.class,0);
		}
		public Variable_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_object; }
	}

	public final Variable_objectContext variable_object() throws RecognitionException {
		Variable_objectContext _localctx = new Variable_objectContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_variable_object);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(OBJECT);
			setState(104);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_DICT:
				{
				setState(97);
				match(LEFT_DICT);
				setState(100);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case DOT:
					{
					setState(98);
					match(DOT);
					}
					break;
				case KEY:
				case RIGHT_DICT:
					{
					setState(99);
					items();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(102);
				match(RIGHT_DICT);
				}
				break;
			case KEY:
			case COLON:
			case RIGHT_DICT:
			case RIGHT_LIST:
			case RIGHT_BUKKET:
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

	public static class Variable_dictContext extends ParserRuleContext {
		public TerminalNode LEFT_DICT() { return getToken(pyon_schemeParser.LEFT_DICT, 0); }
		public Variable_dict_itemsContext variable_dict_items() {
			return getRuleContext(Variable_dict_itemsContext.class,0);
		}
		public TerminalNode RIGHT_DICT() { return getToken(pyon_schemeParser.RIGHT_DICT, 0); }
		public Variable_dictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_dict; }
	}

	public final Variable_dictContext variable_dict() throws RecognitionException {
		Variable_dictContext _localctx = new Variable_dictContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_variable_dict);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(LEFT_DICT);
			setState(107);
			variable_dict_items();
			setState(108);
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
		enterRule(_localctx, 28, RULE_variable_dict_items);
		try {
			setState(114);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				variable_dict_item();
				setState(111);
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
		enterRule(_localctx, 30, RULE_other_variable_dict_items);
		try {
			setState(120);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				variable_dict_item();
				setState(117);
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
		public TerminalNode KEY() { return getToken(pyon_schemeParser.KEY, 0); }
		public TerminalNode COMMA() { return getToken(pyon_schemeParser.COMMA, 0); }
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
		enterRule(_localctx, 32, RULE_variable_dict_item);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(KEY);
			setState(123);
			match(COMMA);
			setState(124);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26\u0081\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3\5"+
		"\5\5\66\n\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7>\n\7\3\b\3\b\3\b\5\bC\n\b\3\t"+
		"\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\nM\n\n\3\13\3\13\3\13\3\13\3\13\5\13T\n"+
		"\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f]\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16"+
		"\3\16\5\16g\n\16\3\16\3\16\5\16k\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3"+
		"\20\3\20\5\20u\n\20\3\21\3\21\3\21\3\21\5\21{\n\21\3\22\3\22\3\22\3\22"+
		"\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\2\2\177\2$\3"+
		"\2\2\2\4&\3\2\2\2\6.\3\2\2\2\b\65\3\2\2\2\n\67\3\2\2\2\f=\3\2\2\2\16?"+
		"\3\2\2\2\20D\3\2\2\2\22L\3\2\2\2\24S\3\2\2\2\26\\\3\2\2\2\30^\3\2\2\2"+
		"\32b\3\2\2\2\34l\3\2\2\2\36t\3\2\2\2 z\3\2\2\2\"|\3\2\2\2$%\5\4\3\2%\3"+
		"\3\2\2\2&\'\7\16\2\2\'(\5\6\4\2()\7\17\2\2)\5\3\2\2\2*+\5\n\6\2+,\5\b"+
		"\5\2,/\3\2\2\2-/\3\2\2\2.*\3\2\2\2.-\3\2\2\2/\7\3\2\2\2\60\61\7\13\2\2"+
		"\61\62\5\n\6\2\62\63\5\b\5\2\63\66\3\2\2\2\64\66\3\2\2\2\65\60\3\2\2\2"+
		"\65\64\3\2\2\2\66\t\3\2\2\2\678\7\b\2\289\7\f\2\29:\5\f\7\2:\13\3\2\2"+
		"\2;>\5\4\3\2<>\5\16\b\2=;\3\2\2\2=<\3\2\2\2>\r\3\2\2\2?B\7\n\2\2@C\5\20"+
		"\t\2AC\5\34\17\2B@\3\2\2\2BA\3\2\2\2C\17\3\2\2\2DE\7\22\2\2EF\5\22\n\2"+
		"FG\7\23\2\2G\21\3\2\2\2HI\5\26\f\2IJ\5\24\13\2JM\3\2\2\2KM\3\2\2\2LH\3"+
		"\2\2\2LK\3\2\2\2M\23\3\2\2\2NO\7\13\2\2OP\5\26\f\2PQ\5\24\13\2QT\3\2\2"+
		"\2RT\3\2\2\2SN\3\2\2\2SR\3\2\2\2T\25\3\2\2\2U]\7\3\2\2V]\7\4\2\2W]\7\5"+
		"\2\2X]\7\6\2\2Y]\7\7\2\2Z]\5\30\r\2[]\5\32\16\2\\U\3\2\2\2\\V\3\2\2\2"+
		"\\W\3\2\2\2\\X\3\2\2\2\\Y\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]\27\3\2\2\2^_"+
		"\7\20\2\2_`\5\22\n\2`a\7\21\2\2a\31\3\2\2\2bj\7\n\2\2cf\7\16\2\2dg\7\r"+
		"\2\2eg\5\6\4\2fd\3\2\2\2fe\3\2\2\2gh\3\2\2\2hk\7\17\2\2ik\3\2\2\2jc\3"+
		"\2\2\2ji\3\2\2\2k\33\3\2\2\2lm\7\16\2\2mn\5\36\20\2no\7\17\2\2o\35\3\2"+
		"\2\2pq\5\"\22\2qr\5 \21\2ru\3\2\2\2su\3\2\2\2tp\3\2\2\2ts\3\2\2\2u\37"+
		"\3\2\2\2vw\5\"\22\2wx\5 \21\2x{\3\2\2\2y{\3\2\2\2zv\3\2\2\2zy\3\2\2\2"+
		"{!\3\2\2\2|}\7\b\2\2}~\7\f\2\2~\177\5\26\f\2\177#\3\2\2\2\r.\65=BLS\\"+
		"fjtz";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}