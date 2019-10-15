// Generated from /home/jiazizhou/antlr/pyon/pyon.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, CTX=6, KEY=7, STRING=8, OBJECT=9, 
		COLON=10, COMMA=11, LEFT_DICT=12, RIGHT_DICT=13, LEFT_LIST=14, RIGHT_LIST=15, 
		LEFT_BUKKET=16, RIGHT_BUKKEFT=17, LINE_COMMENT=18, COMMENT=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"INT", "FLOAT", "TRUE", "FALSE", "NONE", "CTX", "KEY", "ESC_DOUBLE", "ESC_SINGLE", 
		"STRING", "OBJECT", "COLON", "COMMA", "LEFT_DICT", "RIGHT_DICT", "LEFT_LIST", 
		"RIGHT_LIST", "LEFT_BUKKET", "RIGHT_BUKKEFT", "LINE_COMMENT", "COMMENT", 
		"WS"
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


	public pyonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "pyon.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u011b\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\5\2\61\n\2"+
		"\3\2\6\2\64\n\2\r\2\16\2\65\3\3\5\39\n\3\3\3\6\3<\n\3\r\3\16\3=\3\3\3"+
		"\3\7\3B\n\3\f\3\16\3E\13\3\5\3G\n\3\3\3\3\3\6\3K\n\3\r\3\16\3L\5\3O\n"+
		"\3\3\3\3\3\5\3S\n\3\3\3\6\3V\n\3\r\3\16\3W\5\3Z\n\3\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\5\4d\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5p\n"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6z\n\6\3\7\3\7\3\7\3\7\3\b\6\b\u0081"+
		"\n\b\r\b\16\b\u0082\3\b\7\b\u0086\n\b\f\b\16\b\u0089\13\b\3\t\3\t\3\t"+
		"\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13\u0096\n\13\f\13\16\13\u0099"+
		"\13\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00a1\n\13\f\13\16\13\u00a4"+
		"\13\13\3\13\5\13\u00a7\n\13\3\f\6\f\u00aa\n\f\r\f\16\f\u00ab\3\f\7\f\u00af"+
		"\n\f\f\f\16\f\u00b2\13\f\5\f\u00b4\n\f\3\f\3\f\6\f\u00b8\n\f\r\f\16\f"+
		"\u00b9\3\f\7\f\u00bd\n\f\f\f\16\f\u00c0\13\f\3\f\3\f\3\f\7\f\u00c5\n\f"+
		"\f\f\16\f\u00c8\13\f\5\f\u00ca\n\f\3\f\7\f\u00cd\n\f\f\f\16\f\u00d0\13"+
		"\f\3\f\6\f\u00d3\n\f\r\f\16\f\u00d4\3\f\7\f\u00d8\n\f\f\f\16\f\u00db\13"+
		"\f\3\f\3\f\3\f\7\f\u00e0\n\f\f\f\16\f\u00e3\13\f\5\f\u00e5\n\f\3\r\3\r"+
		"\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24"+
		"\3\25\3\25\3\25\3\25\7\25\u00fb\n\25\f\25\16\25\u00fe\13\25\3\25\5\25"+
		"\u0101\n\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u010b\n\26\f"+
		"\26\16\26\u010e\13\26\3\26\3\26\3\26\3\26\3\26\3\27\6\27\u0116\n\27\r"+
		"\27\16\27\u0117\3\27\3\27\6\u0097\u00a2\u00fc\u010c\2\30\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\2\23\2\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22"+
		"\'\23)\24+\25-\26\3\2\n\4\2--//\3\2\62;\4\2GGgg\5\2C\\aac|\6\2\62;C\\"+
		"aac|\b\2$$^^ddppttvv\3\2\63;\5\2\13\f\17\17\"\"\2\u0141\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2"+
		"\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2"+
		"+\3\2\2\2\2-\3\2\2\2\3\60\3\2\2\2\58\3\2\2\2\7c\3\2\2\2\to\3\2\2\2\13"+
		"y\3\2\2\2\r{\3\2\2\2\17\u0080\3\2\2\2\21\u008a\3\2\2\2\23\u008d\3\2\2"+
		"\2\25\u00a6\3\2\2\2\27\u00b3\3\2\2\2\31\u00e6\3\2\2\2\33\u00e8\3\2\2\2"+
		"\35\u00ea\3\2\2\2\37\u00ec\3\2\2\2!\u00ee\3\2\2\2#\u00f0\3\2\2\2%\u00f2"+
		"\3\2\2\2\'\u00f4\3\2\2\2)\u00f6\3\2\2\2+\u0106\3\2\2\2-\u0115\3\2\2\2"+
		"/\61\t\2\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\64\t\3\2\2\63"+
		"\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\4\3\2\2\2\67"+
		"9\t\2\2\28\67\3\2\2\289\3\2\2\29N\3\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3\2\2"+
		"\2=;\3\2\2\2=>\3\2\2\2>F\3\2\2\2?C\7\60\2\2@B\t\3\2\2A@\3\2\2\2BE\3\2"+
		"\2\2CA\3\2\2\2CD\3\2\2\2DG\3\2\2\2EC\3\2\2\2F?\3\2\2\2FG\3\2\2\2GO\3\2"+
		"\2\2HJ\7\60\2\2IK\t\3\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3"+
		"\2\2\2N;\3\2\2\2NH\3\2\2\2OY\3\2\2\2PR\t\4\2\2QS\t\2\2\2RQ\3\2\2\2RS\3"+
		"\2\2\2SU\3\2\2\2TV\t\3\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3"+
		"\2\2\2YP\3\2\2\2YZ\3\2\2\2Z\6\3\2\2\2[\\\7V\2\2\\]\7t\2\2]^\7w\2\2^d\7"+
		"g\2\2_`\7v\2\2`a\7t\2\2ab\7w\2\2bd\7g\2\2c[\3\2\2\2c_\3\2\2\2d\b\3\2\2"+
		"\2ef\7H\2\2fg\7c\2\2gh\7n\2\2hi\7u\2\2ip\7g\2\2jk\7h\2\2kl\7c\2\2lm\7"+
		"n\2\2mn\7u\2\2np\7g\2\2oe\3\2\2\2oj\3\2\2\2p\n\3\2\2\2qr\7P\2\2rs\7q\2"+
		"\2st\7p\2\2tz\7g\2\2uv\7p\2\2vw\7q\2\2wx\7p\2\2xz\7g\2\2yq\3\2\2\2yu\3"+
		"\2\2\2z\f\3\2\2\2{|\7e\2\2|}\7v\2\2}~\7z\2\2~\16\3\2\2\2\177\u0081\t\5"+
		"\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083"+
		"\3\2\2\2\u0083\u0087\3\2\2\2\u0084\u0086\t\6\2\2\u0085\u0084\3\2\2\2\u0086"+
		"\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\20\3\2\2"+
		"\2\u0089\u0087\3\2\2\2\u008a\u008b\7^\2\2\u008b\u008c\7$\2\2\u008c\22"+
		"\3\2\2\2\u008d\u008e\7^\2\2\u008e\u008f\7)\2\2\u008f\24\3\2\2\2\u0090"+
		"\u0097\7$\2\2\u0091\u0096\5\21\t\2\u0092\u0096\13\2\2\2\u0093\u0094\7"+
		"^\2\2\u0094\u0096\t\7\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2\u0095"+
		"\u0093\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0098\3\2\2\2\u0097\u0095\3\2"+
		"\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u00a7\7$\2\2\u009b"+
		"\u00a2\7)\2\2\u009c\u00a1\5\23\n\2\u009d\u00a1\13\2\2\2\u009e\u009f\7"+
		"^\2\2\u009f\u00a1\t\7\2\2\u00a0\u009c\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0"+
		"\u009e\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a2\u00a0\3\2"+
		"\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\7)\2\2\u00a6"+
		"\u0090\3\2\2\2\u00a6\u009b\3\2\2\2\u00a7\26\3\2\2\2\u00a8\u00aa\t\5\2"+
		"\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac"+
		"\3\2\2\2\u00ac\u00b0\3\2\2\2\u00ad\u00af\t\6\2\2\u00ae\u00ad\3\2\2\2\u00af"+
		"\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b4\3\2"+
		"\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00a9\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4"+
		"\u00b5\3\2\2\2\u00b5\u00ce\7B\2\2\u00b6\u00b8\t\5\2\2\u00b7\u00b6\3\2"+
		"\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba"+
		"\u00be\3\2\2\2\u00bb\u00bd\t\6\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2"+
		"\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00ca\3\2\2\2\u00c0"+
		"\u00be\3\2\2\2\u00c1\u00ca\7\62\2\2\u00c2\u00c6\t\b\2\2\u00c3\u00c5\t"+
		"\3\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6"+
		"\u00c7\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00b7\3\2"+
		"\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c2\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb"+
		"\u00cd\7\60\2\2\u00cc\u00c9\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3"+
		"\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00e4\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1"+
		"\u00d3\t\5\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3\2"+
		"\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d9\3\2\2\2\u00d6\u00d8\t\6\2\2\u00d7"+
		"\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2"+
		"\2\2\u00da\u00e5\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e5\7\62\2\2\u00dd"+
		"\u00e1\t\b\2\2\u00de\u00e0\t\3\2\2\u00df\u00de\3\2\2\2\u00e0\u00e3\3\2"+
		"\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3"+
		"\u00e1\3\2\2\2\u00e4\u00d2\3\2\2\2\u00e4\u00dc\3\2\2\2\u00e4\u00dd\3\2"+
		"\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\7.\2\2\u00e7\32\3\2\2\2\u00e8\u00e9"+
		"\7<\2\2\u00e9\34\3\2\2\2\u00ea\u00eb\7}\2\2\u00eb\36\3\2\2\2\u00ec\u00ed"+
		"\7\177\2\2\u00ed \3\2\2\2\u00ee\u00ef\7]\2\2\u00ef\"\3\2\2\2\u00f0\u00f1"+
		"\7_\2\2\u00f1$\3\2\2\2\u00f2\u00f3\7*\2\2\u00f3&\3\2\2\2\u00f4\u00f5\7"+
		"+\2\2\u00f5(\3\2\2\2\u00f6\u00f7\7\61\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00fc"+
		"\3\2\2\2\u00f9\u00fb\13\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2"+
		"\u00fc\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc"+
		"\3\2\2\2\u00ff\u0101\7\17\2\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2"+
		"\u0101\u0102\3\2\2\2\u0102\u0103\7\f\2\2\u0103\u0104\3\2\2\2\u0104\u0105"+
		"\b\25\2\2\u0105*\3\2\2\2\u0106\u0107\7\61\2\2\u0107\u0108\7,\2\2\u0108"+
		"\u010c\3\2\2\2\u0109\u010b\13\2\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3"+
		"\2\2\2\u010c\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f\3\2\2\2\u010e"+
		"\u010c\3\2\2\2\u010f\u0110\7,\2\2\u0110\u0111\7\61\2\2\u0111\u0112\3\2"+
		"\2\2\u0112\u0113\b\26\2\2\u0113,\3\2\2\2\u0114\u0116\t\t\2\2\u0115\u0114"+
		"\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118"+
		"\u0119\3\2\2\2\u0119\u011a\b\27\2\2\u011a.\3\2\2\2(\2\60\658=CFLNRWYc"+
		"oy\u0082\u0087\u0095\u0097\u00a0\u00a2\u00a6\u00ab\u00b0\u00b3\u00b9\u00be"+
		"\u00c6\u00c9\u00ce\u00d4\u00d9\u00e1\u00e4\u00fc\u0100\u010c\u0117\3\b"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}