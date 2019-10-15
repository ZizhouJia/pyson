// Generated from /home/jiazizhou/antlr/pyon_scheme/pyon_scheme.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyon_schemeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, KEY=6, STRING=7, OBJECT=8, COLON=9, 
		COMMA=10, DOT=11, LEFT_DICT=12, RIGHT_DICT=13, LEFT_LIST=14, RIGHT_LIST=15, 
		LEFT_BUKKET=16, RIGHT_BUKKET=17, LINE_COMMENT=18, COMMENT=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"INT", "FLOAT", "TRUE", "FALSE", "NONE", "KEY", "ESC_DOUBLE", "ESC_SINGLE", 
		"STRING", "OBJECT", "COLON", "COMMA", "DOT", "LEFT_DICT", "RIGHT_DICT", 
		"LEFT_LIST", "RIGHT_LIST", "LEFT_BUKKET", "RIGHT_BUKKET", "LINE_COMMENT", 
		"COMMENT", "WS"
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


	public pyon_schemeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "pyon_scheme.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u011a\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\5\2\61\n\2"+
		"\3\2\6\2\64\n\2\r\2\16\2\65\3\3\5\39\n\3\3\3\6\3<\n\3\r\3\16\3=\3\3\3"+
		"\3\7\3B\n\3\f\3\16\3E\13\3\5\3G\n\3\3\3\3\3\6\3K\n\3\r\3\16\3L\5\3O\n"+
		"\3\3\3\3\3\5\3S\n\3\3\3\6\3V\n\3\r\3\16\3W\5\3Z\n\3\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\5\4d\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5p\n"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6z\n\6\3\7\6\7}\n\7\r\7\16\7~\3\7"+
		"\7\7\u0082\n\7\f\7\16\7\u0085\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n"+
		"\3\n\3\n\7\n\u0092\n\n\f\n\16\n\u0095\13\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n"+
		"\u009d\n\n\f\n\16\n\u00a0\13\n\3\n\5\n\u00a3\n\n\3\13\6\13\u00a6\n\13"+
		"\r\13\16\13\u00a7\3\13\7\13\u00ab\n\13\f\13\16\13\u00ae\13\13\5\13\u00b0"+
		"\n\13\3\13\3\13\6\13\u00b4\n\13\r\13\16\13\u00b5\3\13\7\13\u00b9\n\13"+
		"\f\13\16\13\u00bc\13\13\3\13\3\13\3\13\7\13\u00c1\n\13\f\13\16\13\u00c4"+
		"\13\13\3\13\5\13\u00c7\n\13\3\13\7\13\u00ca\n\13\f\13\16\13\u00cd\13\13"+
		"\3\13\6\13\u00d0\n\13\r\13\16\13\u00d1\3\13\7\13\u00d5\n\13\f\13\16\13"+
		"\u00d8\13\13\3\13\3\13\3\13\7\13\u00dd\n\13\f\13\16\13\u00e0\13\13\5\13"+
		"\u00e2\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3"+
		"\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u00fa\n\25\f\25"+
		"\16\25\u00fd\13\25\3\25\5\25\u0100\n\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\7\26\u010a\n\26\f\26\16\26\u010d\13\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\27\6\27\u0115\n\27\r\27\16\27\u0116\3\27\3\27\6\u0093\u009e\u00fb"+
		"\u010b\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\t\25\n\27\13\31\f\33"+
		"\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26\3\2\13\4\2--//\3\2\62;\4\2"+
		"GGgg\5\2C\\aac|\6\2\62;C\\aac|\b\2$$^^ddppttvv\3\2\63;\4\2,,\62\62\5\2"+
		"\13\f\17\17\"\"\2\u0141\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31"+
		"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2"+
		"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\3\60\3\2\2\2"+
		"\58\3\2\2\2\7c\3\2\2\2\to\3\2\2\2\13y\3\2\2\2\r|\3\2\2\2\17\u0086\3\2"+
		"\2\2\21\u0089\3\2\2\2\23\u00a2\3\2\2\2\25\u00af\3\2\2\2\27\u00e3\3\2\2"+
		"\2\31\u00e5\3\2\2\2\33\u00e7\3\2\2\2\35\u00e9\3\2\2\2\37\u00eb\3\2\2\2"+
		"!\u00ed\3\2\2\2#\u00ef\3\2\2\2%\u00f1\3\2\2\2\'\u00f3\3\2\2\2)\u00f5\3"+
		"\2\2\2+\u0105\3\2\2\2-\u0114\3\2\2\2/\61\t\2\2\2\60/\3\2\2\2\60\61\3\2"+
		"\2\2\61\63\3\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2"+
		"\2\2\65\66\3\2\2\2\66\4\3\2\2\2\679\t\2\2\28\67\3\2\2\289\3\2\2\29N\3"+
		"\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>F\3\2\2\2?C\7"+
		"\60\2\2@B\t\3\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DG\3\2\2\2EC"+
		"\3\2\2\2F?\3\2\2\2FG\3\2\2\2GO\3\2\2\2HJ\7\60\2\2IK\t\3\2\2JI\3\2\2\2"+
		"KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2N;\3\2\2\2NH\3\2\2\2OY\3\2\2\2"+
		"PR\t\4\2\2QS\t\2\2\2RQ\3\2\2\2RS\3\2\2\2SU\3\2\2\2TV\t\3\2\2UT\3\2\2\2"+
		"VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YP\3\2\2\2YZ\3\2\2\2Z\6\3\2\2"+
		"\2[\\\7V\2\2\\]\7t\2\2]^\7w\2\2^d\7g\2\2_`\7v\2\2`a\7t\2\2ab\7w\2\2bd"+
		"\7g\2\2c[\3\2\2\2c_\3\2\2\2d\b\3\2\2\2ef\7H\2\2fg\7c\2\2gh\7n\2\2hi\7"+
		"u\2\2ip\7g\2\2jk\7h\2\2kl\7c\2\2lm\7n\2\2mn\7u\2\2np\7g\2\2oe\3\2\2\2"+
		"oj\3\2\2\2p\n\3\2\2\2qr\7P\2\2rs\7q\2\2st\7p\2\2tz\7g\2\2uv\7p\2\2vw\7"+
		"q\2\2wx\7p\2\2xz\7g\2\2yq\3\2\2\2yu\3\2\2\2z\f\3\2\2\2{}\t\5\2\2|{\3\2"+
		"\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0083\3\2\2\2\u0080\u0082\t"+
		"\6\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083"+
		"\u0084\3\2\2\2\u0084\16\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\7^\2\2"+
		"\u0087\u0088\7$\2\2\u0088\20\3\2\2\2\u0089\u008a\7^\2\2\u008a\u008b\7"+
		")\2\2\u008b\22\3\2\2\2\u008c\u0093\7$\2\2\u008d\u0092\5\17\b\2\u008e\u0092"+
		"\13\2\2\2\u008f\u0090\7^\2\2\u0090\u0092\t\7\2\2\u0091\u008d\3\2\2\2\u0091"+
		"\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0094\3\2"+
		"\2\2\u0093\u0091\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096"+
		"\u00a3\7$\2\2\u0097\u009e\7)\2\2\u0098\u009d\5\21\t\2\u0099\u009d\13\2"+
		"\2\2\u009a\u009b\7^\2\2\u009b\u009d\t\7\2\2\u009c\u0098\3\2\2\2\u009c"+
		"\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009f\3\2"+
		"\2\2\u009e\u009c\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1"+
		"\u00a3\7)\2\2\u00a2\u008c\3\2\2\2\u00a2\u0097\3\2\2\2\u00a3\24\3\2\2\2"+
		"\u00a4\u00a6\t\5\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5"+
		"\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ac\3\2\2\2\u00a9\u00ab\t\6\2\2\u00aa"+
		"\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2"+
		"\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00a5\3\2\2\2\u00af"+
		"\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00cb\7B\2\2\u00b2\u00b4\t\5"+
		"\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5"+
		"\u00b6\3\2\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9\t\6\2\2\u00b8\u00b7\3\2"+
		"\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb"+
		"\u00c7\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00c7\7\62\2\2\u00be\u00c2\t"+
		"\b\2\2\u00bf\u00c1\t\3\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2"+
		"\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c2\3\2"+
		"\2\2\u00c5\u00c7\7,\2\2\u00c6\u00b3\3\2\2\2\u00c6\u00bd\3\2\2\2\u00c6"+
		"\u00be\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\7\60"+
		"\2\2\u00c9\u00c6\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb"+
		"\u00cc\3\2\2\2\u00cc\u00e1\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d0\t\5"+
		"\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1"+
		"\u00d2\3\2\2\2\u00d2\u00d6\3\2\2\2\u00d3\u00d5\t\6\2\2\u00d4\u00d3\3\2"+
		"\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7"+
		"\u00e2\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00e2\t\t\2\2\u00da\u00de\t\b"+
		"\2\2\u00db\u00dd\t\3\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de"+
		"\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2"+
		"\2\2\u00e1\u00cf\3\2\2\2\u00e1\u00d9\3\2\2\2\u00e1\u00da\3\2\2\2\u00e2"+
		"\26\3\2\2\2\u00e3\u00e4\7.\2\2\u00e4\30\3\2\2\2\u00e5\u00e6\7<\2\2\u00e6"+
		"\32\3\2\2\2\u00e7\u00e8\7\60\2\2\u00e8\34\3\2\2\2\u00e9\u00ea\7}\2\2\u00ea"+
		"\36\3\2\2\2\u00eb\u00ec\7\177\2\2\u00ec \3\2\2\2\u00ed\u00ee\7]\2\2\u00ee"+
		"\"\3\2\2\2\u00ef\u00f0\7_\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7*\2\2\u00f2"+
		"&\3\2\2\2\u00f3\u00f4\7+\2\2\u00f4(\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6"+
		"\u00f7\7\61\2\2\u00f7\u00fb\3\2\2\2\u00f8\u00fa\13\2\2\2\u00f9\u00f8\3"+
		"\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc"+
		"\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0100\7\17\2\2\u00ff\u00fe\3"+
		"\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7\f\2\2\u0102"+
		"\u0103\3\2\2\2\u0103\u0104\b\25\2\2\u0104*\3\2\2\2\u0105\u0106\7\61\2"+
		"\2\u0106\u0107\7,\2\2\u0107\u010b\3\2\2\2\u0108\u010a\13\2\2\2\u0109\u0108"+
		"\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c"+
		"\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\7,\2\2\u010f\u0110\7\61"+
		"\2\2\u0110\u0111\3\2\2\2\u0111\u0112\b\26\2\2\u0112,\3\2\2\2\u0113\u0115"+
		"\t\n\2\2\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116"+
		"\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\b\27\2\2\u0119.\3\2\2\2"+
		"(\2\60\658=CFLNRWYcoy~\u0083\u0091\u0093\u009c\u009e\u00a2\u00a7\u00ac"+
		"\u00af\u00b5\u00ba\u00c2\u00c6\u00cb\u00d1\u00d6\u00de\u00e1\u00fb\u00ff"+
		"\u010b\u0116\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}