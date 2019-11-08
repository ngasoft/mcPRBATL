# Generated from C:/Users/ac1222/OneDrive - Coventry University/GitHub/mcPRBATL/mcprbatl/parser/grammar\PRBATLFormula.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00ae\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\7\26z\n\26\f\26\16\26}\13\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\6\30\u0084\n\30\r\30\16\30\u0085\5\30\u0088\n\30\3\30")
        buf.write("\3\30\3\30\7\30\u008d\n\30\f\30\16\30\u0090\13\30\3\30")
        buf.write("\3\30\5\30\u0094\n\30\3\31\3\31\3\32\3\32\7\32\u009a\n")
        buf.write("\32\f\32\16\32\u009d\13\32\3\33\6\33\u00a0\n\33\r\33\16")
        buf.write("\33\u00a1\3\33\3\33\3\34\3\34\7\34\u00a8\n\34\f\34\16")
        buf.write("\34\u00ab\13\34\3\34\3\34\2\2\35\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\35\3\2\b\3\2\63;\3\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\4\2\f\f\17\17\2\u00b5\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2\2\2")
        buf.write("\5;\3\2\2\2\7=\3\2\2\2\t?\3\2\2\2\13A\3\2\2\2\rC\3\2\2")
        buf.write("\2\17H\3\2\2\2\21O\3\2\2\2\23U\3\2\2\2\25W\3\2\2\2\27")
        buf.write("Y\3\2\2\2\31\\\3\2\2\2\33_\3\2\2\2\35a\3\2\2\2\37c\3\2")
        buf.write("\2\2!e\3\2\2\2#i\3\2\2\2%n\3\2\2\2\'q\3\2\2\2)t\3\2\2")
        buf.write("\2+w\3\2\2\2-~\3\2\2\2/\u0093\3\2\2\2\61\u0095\3\2\2\2")
        buf.write("\63\u0097\3\2\2\2\65\u009f\3\2\2\2\67\u00a5\3\2\2\29:")
        buf.write("\7`\2\2:\4\3\2\2\2;<\7}\2\2<\6\3\2\2\2=>\7.\2\2>\b\3\2")
        buf.write("\2\2?@\7\177\2\2@\n\3\2\2\2AB\7,\2\2B\f\3\2\2\2CD\7P\2")
        buf.write("\2DE\7g\2\2EF\7z\2\2FG\7v\2\2G\16\3\2\2\2HI\7W\2\2IJ\7")
        buf.write("p\2\2JK\7v\2\2KL\7k\2\2LM\7n\2\2MN\7`\2\2N\20\3\2\2\2")
        buf.write("OP\7W\2\2PQ\7p\2\2QR\7v\2\2RS\7k\2\2ST\7n\2\2T\22\3\2")
        buf.write("\2\2UV\7>\2\2V\24\3\2\2\2WX\7@\2\2X\26\3\2\2\2YZ\7?\2")
        buf.write("\2Z[\7>\2\2[\30\3\2\2\2\\]\7@\2\2]^\7?\2\2^\32\3\2\2\2")
        buf.write("_`\7*\2\2`\34\3\2\2\2ab\7+\2\2b\36\3\2\2\2cd\7V\2\2d ")
        buf.write("\3\2\2\2ef\7p\2\2fg\7q\2\2gh\7v\2\2h\"\3\2\2\2ij\7r\2")
        buf.write("\2jk\7t\2\2kl\7q\2\2lm\7d\2\2m$\3\2\2\2no\7q\2\2op\7t")
        buf.write("\2\2p&\3\2\2\2qr\7>\2\2rs\7>\2\2s(\3\2\2\2tu\7@\2\2uv")
        buf.write("\7@\2\2v*\3\2\2\2w{\t\2\2\2xz\t\3\2\2yx\3\2\2\2z}\3\2")
        buf.write("\2\2{y\3\2\2\2{|\3\2\2\2|,\3\2\2\2}{\3\2\2\2~\177\7\62")
        buf.write("\2\2\177.\3\2\2\2\u0080\u0087\5+\26\2\u0081\u0083\7\60")
        buf.write("\2\2\u0082\u0084\t\3\2\2\u0083\u0082\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0088\3\2\2\2\u0087\u0081\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0094\3\2\2\2\u0089\u008a\5-\27\2\u008a\u008e\7")
        buf.write("\60\2\2\u008b\u008d\t\3\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\t")
        buf.write("\2\2\2\u0092\u0094\3\2\2\2\u0093\u0080\3\2\2\2\u0093\u0089")
        buf.write("\3\2\2\2\u0094\60\3\2\2\2\u0095\u0096\5\63\32\2\u0096")
        buf.write("\62\3\2\2\2\u0097\u009b\t\4\2\2\u0098\u009a\t\5\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\64\3\2\2\2\u009d\u009b\3\2")
        buf.write("\2\2\u009e\u00a0\t\6\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a4\b\33\2\2\u00a4\66\3\2\2\2\u00a5")
        buf.write("\u00a9\7%\2\2\u00a6\u00a8\n\7\2\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad")
        buf.write("\b\34\2\2\u00ad8\3\2\2\2\13\2{\u0085\u0087\u008e\u0093")
        buf.write("\u009b\u00a1\u00a9\3\b\2\2")
        return buf.getvalue()


class PRBATLFormulaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    LT_OP = 9
    GT_OP = 10
    LEQ_OP = 11
    GEQ_OP = 12
    OPEN = 13
    CLOSE = 14
    TOP = 15
    NOT = 16
    PROB = 17
    OR = 18
    OPEN_AGENT = 19
    CLOSE_AGENT = 20
    POSITIVE_NUMBER = 21
    NUMBER_0 = 22
    POSITIVE_REAL_NUMBER = 23
    PROPOSITION = 24
    NAME = 25
    WS = 26
    LINE_COMMENT = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'^'", "'{'", "','", "'}'", "'*'", "'Next'", "'Until^'", "'Until'", 
            "'<'", "'>'", "'=<'", "'>='", "'('", "')'", "'T'", "'not'", 
            "'prob'", "'or'", "'<<'", "'>>'", "'0'" ]

    symbolicNames = [ "<INVALID>",
            "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "OPEN", "CLOSE", "TOP", 
            "NOT", "PROB", "OR", "OPEN_AGENT", "CLOSE_AGENT", "POSITIVE_NUMBER", 
            "NUMBER_0", "POSITIVE_REAL_NUMBER", "PROPOSITION", "NAME", "WS", 
            "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "OPEN", 
                  "CLOSE", "TOP", "NOT", "PROB", "OR", "OPEN_AGENT", "CLOSE_AGENT", 
                  "POSITIVE_NUMBER", "NUMBER_0", "POSITIVE_REAL_NUMBER", 
                  "PROPOSITION", "NAME", "WS", "LINE_COMMENT" ]

    grammarFileName = "PRBATLFormula.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


