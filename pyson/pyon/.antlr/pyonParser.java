// Generated from /home/jiazizhou/antlr/pyon/pyon.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, CTX=6, KEY=7, STRING=8, OBJECT=9, 
		COLON=10, COMMA=11, LEFT_DICT=12, RIGHT_DICT=13, LEFT_LIST=14, RIGHT_LIST=15, 
		LEFT_BUKKET=16, RIGHT_BUKKEFT=17, LINE_COMMENT=18, COMMENT=19, WS=20;
	public static final int
		RULE_entry_point = 0, RULE_item_dict = 1, RULE_items = 2, RULE_other_items = 3, 
		RULE_item = 4, RULE_value = 5, RULE_values = 6, RULE_other_values = 7, 
		RULE_item_list = 8, RULE_item_tuple = 9, RULE_item_object = 10;
	public static final String[] ruleNames = {
		"entry_point", "item_dict", "items", "other_items", "item", "value", "values", 
		"other_values", "item_list", "item_tuple", "item_object"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, "'ctx'", null, null, null, "','", 
		"':'", "'{'", "'}'", "'['", "']'", "'('", "')'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "INT", "FLOAT", "TRUE", "FALSE", "NONE", "CTX", "KEY", "STRING", 
		"OBJECT", "COLON", "COMMA", "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", "RIGHT_LIST", 
		"LEFT_BUKKET", "RIGHT_BUKKEFT", "LINE_COMMENT", "COMMENT", "WS"
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
	public String getGrammarFileName() { return "pyon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pyonParser(TokenStream input) {
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
			setState(22);
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
		public TerminalNode LEFT_DICT() { return getToken(pyonParser.LEFT_DICT, 0); }
		public ItemsContext items() {
			return getRuleContext(ItemsContext.class,0);
		}
		public TerminalNode RIGHT_DICT() { return getToken(pyonParser.RIGHT_DICT, 0); }
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
			setState(24);
			match(LEFT_DICT);
			setState(25);
			items();
			setState(26);
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
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				item();
				setState(29);
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
		public TerminalNode COLON() { return getToken(pyonParser.COLON, 0); }
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
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(COLON);
				setState(35);
				item();
				setState(36);
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
		public TerminalNode KEY() { return getToken(pyonParser.KEY, 0); }
		public TerminalNode COMMA() { return getToken(pyonParser.COMMA, 0); }
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
			setState(41);
			match(KEY);
			setState(42);
			match(COMMA);
			setState(43);
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
		public TerminalNode INT() { return getToken(pyonParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(pyonParser.FLOAT, 0); }
		public TerminalNode TRUE() { return getToken(pyonParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(pyonParser.FALSE, 0); }
		public TerminalNode NONE() { return getToken(pyonParser.NONE, 0); }
		public TerminalNode STRING() { return getToken(pyonParser.STRING, 0); }
		public TerminalNode CTX() { return getToken(pyonParser.CTX, 0); }
		public Item_dictContext item_dict() {
			return getRuleContext(Item_dictContext.class,0);
		}
		public Item_listContext item_list() {
			return getRuleContext(Item_listContext.class,0);
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
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				match(FLOAT);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 3);
				{
				setState(47);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(48);
				match(FALSE);
				}
				break;
			case NONE:
				enterOuterAlt(_localctx, 5);
				{
				setState(49);
				match(NONE);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 6);
				{
				setState(50);
				match(STRING);
				}
				break;
			case CTX:
				enterOuterAlt(_localctx, 7);
				{
				setState(51);
				match(CTX);
				}
				break;
			case LEFT_DICT:
				enterOuterAlt(_localctx, 8);
				{
				setState(52);
				item_dict();
				}
				break;
			case LEFT_LIST:
				enterOuterAlt(_localctx, 9);
				{
				setState(53);
				item_list();
				}
				break;
			case OBJECT:
				enterOuterAlt(_localctx, 10);
				{
				setState(54);
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

	public static class ValuesContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Other_valuesContext other_values() {
			return getRuleContext(Other_valuesContext.class,0);
		}
		public ValuesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_values; }
	}

	public final ValuesContext values() throws RecognitionException {
		ValuesContext _localctx = new ValuesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_values);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case TRUE:
			case FALSE:
			case NONE:
			case CTX:
			case STRING:
			case OBJECT:
			case LEFT_DICT:
			case LEFT_LIST:
				enterOuterAlt(_localctx, 1);
				{
				setState(57);
				value();
				setState(58);
				other_values();
				}
				break;
			case RIGHT_LIST:
			case RIGHT_BUKKEFT:
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

	public static class Other_valuesContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(pyonParser.COLON, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Other_valuesContext other_values() {
			return getRuleContext(Other_valuesContext.class,0);
		}
		public Other_valuesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other_values; }
	}

	public final Other_valuesContext other_values() throws RecognitionException {
		Other_valuesContext _localctx = new Other_valuesContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_other_values);
		try {
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				match(COLON);
				setState(64);
				value();
				setState(65);
				other_values();
				}
				break;
			case RIGHT_LIST:
			case RIGHT_BUKKEFT:
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

	public static class Item_listContext extends ParserRuleContext {
		public TerminalNode LEFT_LIST() { return getToken(pyonParser.LEFT_LIST, 0); }
		public ValuesContext values() {
			return getRuleContext(ValuesContext.class,0);
		}
		public TerminalNode RIGHT_LIST() { return getToken(pyonParser.RIGHT_LIST, 0); }
		public Item_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_list; }
	}

	public final Item_listContext item_list() throws RecognitionException {
		Item_listContext _localctx = new Item_listContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_item_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(LEFT_LIST);
			setState(71);
			values();
			setState(72);
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

	public static class Item_tupleContext extends ParserRuleContext {
		public TerminalNode LEFT_BUKKET() { return getToken(pyonParser.LEFT_BUKKET, 0); }
		public ValuesContext values() {
			return getRuleContext(ValuesContext.class,0);
		}
		public TerminalNode RIGHT_BUKKEFT() { return getToken(pyonParser.RIGHT_BUKKEFT, 0); }
		public Item_tupleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_tuple; }
	}

	public final Item_tupleContext item_tuple() throws RecognitionException {
		Item_tupleContext _localctx = new Item_tupleContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_item_tuple);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(LEFT_BUKKET);
			setState(75);
			values();
			setState(76);
			match(RIGHT_BUKKEFT);
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
		public TerminalNode OBJECT() { return getToken(pyonParser.OBJECT, 0); }
		public Item_dictContext item_dict() {
			return getRuleContext(Item_dictContext.class,0);
		}
		public Item_tupleContext item_tuple() {
			return getRuleContext(Item_tupleContext.class,0);
		}
		public Item_objectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item_object; }
	}

	public final Item_objectContext item_object() throws RecognitionException {
		Item_objectContext _localctx = new Item_objectContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_item_object);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(OBJECT);
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_DICT:
				{
				setState(79);
				item_dict();
				}
				break;
			case LEFT_BUKKET:
				{
				setState(80);
				item_tuple();
				}
				break;
			case COLON:
			case RIGHT_DICT:
			case RIGHT_LIST:
			case RIGHT_BUKKEFT:
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26W\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\3\5\3\5\3"+
		"\5\3\5\5\5*\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\5\7:\n\7\3\b\3\b\3\b\3\b\5\b@\n\b\3\t\3\t\3\t\3\t\3\t\5\tG\n\t\3\n"+
		"\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fU\n\f\3\f\2\2\r\2"+
		"\4\6\b\n\f\16\20\22\24\26\2\2\2Z\2\30\3\2\2\2\4\32\3\2\2\2\6\"\3\2\2\2"+
		"\b)\3\2\2\2\n+\3\2\2\2\f9\3\2\2\2\16?\3\2\2\2\20F\3\2\2\2\22H\3\2\2\2"+
		"\24L\3\2\2\2\26P\3\2\2\2\30\31\5\4\3\2\31\3\3\2\2\2\32\33\7\16\2\2\33"+
		"\34\5\6\4\2\34\35\7\17\2\2\35\5\3\2\2\2\36\37\5\n\6\2\37 \5\b\5\2 #\3"+
		"\2\2\2!#\3\2\2\2\"\36\3\2\2\2\"!\3\2\2\2#\7\3\2\2\2$%\7\f\2\2%&\5\n\6"+
		"\2&\'\5\b\5\2\'*\3\2\2\2(*\3\2\2\2)$\3\2\2\2)(\3\2\2\2*\t\3\2\2\2+,\7"+
		"\t\2\2,-\7\r\2\2-.\5\f\7\2.\13\3\2\2\2/:\7\3\2\2\60:\7\4\2\2\61:\7\5\2"+
		"\2\62:\7\6\2\2\63:\7\7\2\2\64:\7\n\2\2\65:\7\b\2\2\66:\5\4\3\2\67:\5\22"+
		"\n\28:\5\26\f\29/\3\2\2\29\60\3\2\2\29\61\3\2\2\29\62\3\2\2\29\63\3\2"+
		"\2\29\64\3\2\2\29\65\3\2\2\29\66\3\2\2\29\67\3\2\2\298\3\2\2\2:\r\3\2"+
		"\2\2;<\5\f\7\2<=\5\20\t\2=@\3\2\2\2>@\3\2\2\2?;\3\2\2\2?>\3\2\2\2@\17"+
		"\3\2\2\2AB\7\f\2\2BC\5\f\7\2CD\5\20\t\2DG\3\2\2\2EG\3\2\2\2FA\3\2\2\2"+
		"FE\3\2\2\2G\21\3\2\2\2HI\7\20\2\2IJ\5\16\b\2JK\7\21\2\2K\23\3\2\2\2LM"+
		"\7\22\2\2MN\5\16\b\2NO\7\23\2\2O\25\3\2\2\2PT\7\13\2\2QU\5\4\3\2RU\5\24"+
		"\13\2SU\3\2\2\2TQ\3\2\2\2TR\3\2\2\2TS\3\2\2\2U\27\3\2\2\2\b\")9?FT";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}