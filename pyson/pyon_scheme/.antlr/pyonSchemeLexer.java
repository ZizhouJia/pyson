// Generated from /home/jiazizhou/antlr/pyon_scheme/pyonScheme.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pyonSchemeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, TRUE=3, FALSE=4, NONE=5, KEY=6, STRING=7, OBJECT=8, CHECKER=9, 
		COLON=10, COMMA=11, DOT=12, LEFT_DICT=13, RIGHT_DICT=14, LEFT_LIST=15, 
		RIGHT_LIST=16, LEFT_BUKKET=17, RIGHT_BUKKET=18, LINE_COMMENT=19, COMMENT=20, 
		WS=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"INT", "FLOAT", "TRUE", "FALSE", "NONE", "KEY", "ESC_DOUBLE", "ESC_SINGLE", 
		"STRING", "OBJECT", "CHECKER", "COLON", "COMMA", "DOT", "LEFT_DICT", "RIGHT_DICT", 
		"LEFT_LIST", "RIGHT_LIST", "LEFT_BUKKET", "RIGHT_BUKKET", "LINE_COMMENT", 
		"COMMENT", "WS"
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


	public pyonSchemeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "pyonScheme.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27\u015a\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2"+
		"\5\2\63\n\2\3\2\6\2\66\n\2\r\2\16\2\67\3\3\5\3;\n\3\3\3\6\3>\n\3\r\3\16"+
		"\3?\3\3\3\3\7\3D\n\3\f\3\16\3G\13\3\5\3I\n\3\3\3\3\3\6\3M\n\3\r\3\16\3"+
		"N\5\3Q\n\3\3\3\3\3\5\3U\n\3\3\3\6\3X\n\3\r\3\16\3Y\5\3\\\n\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\5\4f\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\5\5r\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6|\n\6\3\7\6\7\177\n\7\r"+
		"\7\16\7\u0080\3\7\7\7\u0084\n\7\f\7\16\7\u0087\13\7\3\b\3\b\3\b\3\t\3"+
		"\t\3\t\3\n\3\n\3\n\3\n\3\n\7\n\u0094\n\n\f\n\16\n\u0097\13\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\7\n\u009f\n\n\f\n\16\n\u00a2\13\n\3\n\5\n\u00a5\n\n\3\13"+
		"\6\13\u00a8\n\13\r\13\16\13\u00a9\3\13\7\13\u00ad\n\13\f\13\16\13\u00b0"+
		"\13\13\5\13\u00b2\n\13\3\13\3\13\6\13\u00b6\n\13\r\13\16\13\u00b7\3\13"+
		"\7\13\u00bb\n\13\f\13\16\13\u00be\13\13\3\13\3\13\3\13\7\13\u00c3\n\13"+
		"\f\13\16\13\u00c6\13\13\3\13\5\13\u00c9\n\13\3\13\7\13\u00cc\n\13\f\13"+
		"\16\13\u00cf\13\13\3\13\6\13\u00d2\n\13\r\13\16\13\u00d3\3\13\7\13\u00d7"+
		"\n\13\f\13\16\13\u00da\13\13\3\13\3\13\3\13\7\13\u00df\n\13\f\13\16\13"+
		"\u00e2\13\13\5\13\u00e4\n\13\3\f\6\f\u00e7\n\f\r\f\16\f\u00e8\3\f\7\f"+
		"\u00ec\n\f\f\f\16\f\u00ef\13\f\5\f\u00f1\n\f\3\f\3\f\6\f\u00f5\n\f\r\f"+
		"\16\f\u00f6\3\f\7\f\u00fa\n\f\f\f\16\f\u00fd\13\f\3\f\3\f\3\f\7\f\u0102"+
		"\n\f\f\f\16\f\u0105\13\f\5\f\u0107\n\f\3\f\7\f\u010a\n\f\f\f\16\f\u010d"+
		"\13\f\3\f\6\f\u0110\n\f\r\f\16\f\u0111\3\f\7\f\u0115\n\f\f\f\16\f\u0118"+
		"\13\f\3\f\3\f\3\f\7\f\u011d\n\f\f\f\16\f\u0120\13\f\5\f\u0122\n\f\3\r"+
		"\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24"+
		"\3\24\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u013a\n\26\f\26\16\26\u013d\13"+
		"\26\3\26\5\26\u0140\n\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27"+
		"\u014a\n\27\f\27\16\27\u014d\13\27\3\27\3\27\3\27\3\27\3\27\3\30\6\30"+
		"\u0155\n\30\r\30\16\30\u0156\3\30\3\30\6\u0095\u00a0\u013b\u014b\2\31"+
		"\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\t\25\n\27\13\31\f\33\r\35\16\37"+
		"\17!\20#\21%\22\'\23)\24+\25-\26/\27\3\2\13\4\2--//\3\2\62;\4\2GGgg\5"+
		"\2C\\aac|\6\2\62;C\\aac|\b\2$$^^ddppttvv\3\2\63;\4\2,,\62\62\5\2\13\f"+
		"\17\17\"\"\2\u018f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2"+
		"\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2"+
		"\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\62\3\2"+
		"\2\2\5:\3\2\2\2\7e\3\2\2\2\tq\3\2\2\2\13{\3\2\2\2\r~\3\2\2\2\17\u0088"+
		"\3\2\2\2\21\u008b\3\2\2\2\23\u00a4\3\2\2\2\25\u00b1\3\2\2\2\27\u00f0\3"+
		"\2\2\2\31\u0123\3\2\2\2\33\u0125\3\2\2\2\35\u0127\3\2\2\2\37\u0129\3\2"+
		"\2\2!\u012b\3\2\2\2#\u012d\3\2\2\2%\u012f\3\2\2\2\'\u0131\3\2\2\2)\u0133"+
		"\3\2\2\2+\u0135\3\2\2\2-\u0145\3\2\2\2/\u0154\3\2\2\2\61\63\t\2\2\2\62"+
		"\61\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66"+
		"\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\4\3\2\2\29;\t\2\2\2:9\3\2\2\2:"+
		";\3\2\2\2;P\3\2\2\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2"+
		"@H\3\2\2\2AE\7\60\2\2BD\t\3\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2"+
		"\2FI\3\2\2\2GE\3\2\2\2HA\3\2\2\2HI\3\2\2\2IQ\3\2\2\2JL\7\60\2\2KM\t\3"+
		"\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2P=\3\2\2\2PJ\3\2"+
		"\2\2Q[\3\2\2\2RT\t\4\2\2SU\t\2\2\2TS\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\t\3"+
		"\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[R\3\2\2\2[\\\3"+
		"\2\2\2\\\6\3\2\2\2]^\7V\2\2^_\7t\2\2_`\7w\2\2`f\7g\2\2ab\7v\2\2bc\7t\2"+
		"\2cd\7w\2\2df\7g\2\2e]\3\2\2\2ea\3\2\2\2f\b\3\2\2\2gh\7H\2\2hi\7c\2\2"+
		"ij\7n\2\2jk\7u\2\2kr\7g\2\2lm\7h\2\2mn\7c\2\2no\7n\2\2op\7u\2\2pr\7g\2"+
		"\2qg\3\2\2\2ql\3\2\2\2r\n\3\2\2\2st\7P\2\2tu\7q\2\2uv\7p\2\2v|\7g\2\2"+
		"wx\7p\2\2xy\7q\2\2yz\7p\2\2z|\7g\2\2{s\3\2\2\2{w\3\2\2\2|\f\3\2\2\2}\177"+
		"\t\5\2\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2"+
		"\2\u0081\u0085\3\2\2\2\u0082\u0084\t\6\2\2\u0083\u0082\3\2\2\2\u0084\u0087"+
		"\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\16\3\2\2\2\u0087"+
		"\u0085\3\2\2\2\u0088\u0089\7^\2\2\u0089\u008a\7$\2\2\u008a\20\3\2\2\2"+
		"\u008b\u008c\7^\2\2\u008c\u008d\7)\2\2\u008d\22\3\2\2\2\u008e\u0095\7"+
		"$\2\2\u008f\u0094\5\17\b\2\u0090\u0094\13\2\2\2\u0091\u0092\7^\2\2\u0092"+
		"\u0094\t\7\2\2\u0093\u008f\3\2\2\2\u0093\u0090\3\2\2\2\u0093\u0091\3\2"+
		"\2\2\u0094\u0097\3\2\2\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096"+
		"\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u00a5\7$\2\2\u0099\u00a0\7)\2"+
		"\2\u009a\u009f\5\21\t\2\u009b\u009f\13\2\2\2\u009c\u009d\7^\2\2\u009d"+
		"\u009f\t\7\2\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2"+
		"\2\2\u009f\u00a2\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1"+
		"\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a5\7)\2\2\u00a4\u008e\3\2"+
		"\2\2\u00a4\u0099\3\2\2\2\u00a5\24\3\2\2\2\u00a6\u00a8\t\5\2\2\u00a7\u00a6"+
		"\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa"+
		"\u00ae\3\2\2\2\u00ab\u00ad\t\6\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2"+
		"\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0"+
		"\u00ae\3\2\2\2\u00b1\u00a7\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2"+
		"\2\2\u00b3\u00cd\7B\2\2\u00b4\u00b6\t\5\2\2\u00b5\u00b4\3\2\2\2\u00b6"+
		"\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bc\3\2"+
		"\2\2\u00b9\u00bb\t\6\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc"+
		"\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c9\3\2\2\2\u00be\u00bc\3\2"+
		"\2\2\u00bf\u00c9\7\62\2\2\u00c0\u00c4\t\b\2\2\u00c1\u00c3\t\3\2\2\u00c2"+
		"\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2"+
		"\2\2\u00c5\u00c9\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c9\7,\2\2\u00c8"+
		"\u00b5\3\2\2\2\u00c8\u00bf\3\2\2\2\u00c8\u00c0\3\2\2\2\u00c8\u00c7\3\2"+
		"\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\7\60\2\2\u00cb\u00c8\3\2\2\2\u00cc"+
		"\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00e3\3\2"+
		"\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d2\t\5\2\2\u00d1\u00d0\3\2\2\2\u00d2"+
		"\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d8\3\2"+
		"\2\2\u00d5\u00d7\t\6\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8"+
		"\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00e4\3\2\2\2\u00da\u00d8\3\2"+
		"\2\2\u00db\u00e4\t\t\2\2\u00dc\u00e0\t\b\2\2\u00dd\u00df\t\3\2\2\u00de"+
		"\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2"+
		"\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00d1\3\2\2\2\u00e3"+
		"\u00db\3\2\2\2\u00e3\u00dc\3\2\2\2\u00e4\26\3\2\2\2\u00e5\u00e7\t\5\2"+
		"\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9"+
		"\3\2\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00ec\t\6\2\2\u00eb\u00ea\3\2\2\2\u00ec"+
		"\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f1\3\2"+
		"\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e6\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1"+
		"\u00f2\3\2\2\2\u00f2\u010b\7%\2\2\u00f3\u00f5\t\5\2\2\u00f4\u00f3\3\2"+
		"\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7"+
		"\u00fb\3\2\2\2\u00f8\u00fa\t\6\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2"+
		"\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u0107\3\2\2\2\u00fd"+
		"\u00fb\3\2\2\2\u00fe\u0107\7\62\2\2\u00ff\u0103\t\b\2\2\u0100\u0102\t"+
		"\3\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103"+
		"\u0104\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u00f4\3\2"+
		"\2\2\u0106\u00fe\3\2\2\2\u0106\u00ff\3\2\2\2\u0107\u0108\3\2\2\2\u0108"+
		"\u010a\7\60\2\2\u0109\u0106\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3"+
		"\2\2\2\u010b\u010c\3\2\2\2\u010c\u0121\3\2\2\2\u010d\u010b\3\2\2\2\u010e"+
		"\u0110\t\5\2\2\u010f\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2"+
		"\2\2\u0111\u0112\3\2\2\2\u0112\u0116\3\2\2\2\u0113\u0115\t\6\2\2\u0114"+
		"\u0113\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2"+
		"\2\2\u0117\u0122\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u0122\7\62\2\2\u011a"+
		"\u011e\t\b\2\2\u011b\u011d\t\3\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2"+
		"\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0122\3\2\2\2\u0120"+
		"\u011e\3\2\2\2\u0121\u010f\3\2\2\2\u0121\u0119\3\2\2\2\u0121\u011a\3\2"+
		"\2\2\u0122\30\3\2\2\2\u0123\u0124\7.\2\2\u0124\32\3\2\2\2\u0125\u0126"+
		"\7<\2\2\u0126\34\3\2\2\2\u0127\u0128\7\60\2\2\u0128\36\3\2\2\2\u0129\u012a"+
		"\7}\2\2\u012a \3\2\2\2\u012b\u012c\7\177\2\2\u012c\"\3\2\2\2\u012d\u012e"+
		"\7]\2\2\u012e$\3\2\2\2\u012f\u0130\7_\2\2\u0130&\3\2\2\2\u0131\u0132\7"+
		"*\2\2\u0132(\3\2\2\2\u0133\u0134\7+\2\2\u0134*\3\2\2\2\u0135\u0136\7\61"+
		"\2\2\u0136\u0137\7\61\2\2\u0137\u013b\3\2\2\2\u0138\u013a\13\2\2\2\u0139"+
		"\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u013c\3\2\2\2\u013b\u0139\3\2"+
		"\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0140\7\17\2\2\u013f"+
		"\u013e\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\7\f"+
		"\2\2\u0142\u0143\3\2\2\2\u0143\u0144\b\26\2\2\u0144,\3\2\2\2\u0145\u0146"+
		"\7\61\2\2\u0146\u0147\7,\2\2\u0147\u014b\3\2\2\2\u0148\u014a\13\2\2\2"+
		"\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u014c\3\2\2\2\u014b\u0149"+
		"\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7,\2\2\u014f"+
		"\u0150\7\61\2\2\u0150\u0151\3\2\2\2\u0151\u0152\b\27\2\2\u0152.\3\2\2"+
		"\2\u0153\u0155\t\n\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154"+
		"\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\b\30\2\2"+
		"\u0159\60\3\2\2\2\64\2\62\67:?EHNPTY[eq{\u0080\u0085\u0093\u0095\u009e"+
		"\u00a0\u00a4\u00a9\u00ae\u00b1\u00b7\u00bc\u00c4\u00c8\u00cd\u00d3\u00d8"+
		"\u00e0\u00e3\u00e8\u00ed\u00f0\u00f6\u00fb\u0103\u0106\u010b\u0111\u0116"+
		"\u011e\u0121\u013b\u013f\u014b\u0156\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}