# Generated from C:/Users/ac1222/OneDrive - Coventry University/GitHub/mcPRBATL/mcprbatl/parser/grammar\PRBATLFormula.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u009a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\7\2.\n\2\f\2\16\2\61")
        buf.write("\13\2\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\3\3\3\3\3\7\3")
        buf.write(">\n\3\f\3\16\3A\13\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7U\n\7\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t_\n\t\f\t\16\tb\13\t\5\t")
        buf.write("d\n\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\7\13n\n\13\f")
        buf.write("\13\16\13q\13\13\5\13s\n\13\3\13\3\13\3\f\3\f\5\fy\n\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\5\17\u0082\n\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\5\21\u008a\n\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\2\3\4\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*\2\5\3\2\23\26\3\2\27\30\3\2\27\31\2\u0093\2")
        buf.write("/\3\2\2\2\48\3\2\2\2\6B\3\2\2\2\bF\3\2\2\2\nH\3\2\2\2")
        buf.write("\fK\3\2\2\2\16X\3\2\2\2\20Z\3\2\2\2\22g\3\2\2\2\24i\3")
        buf.write("\2\2\2\26x\3\2\2\2\30z\3\2\2\2\32|\3\2\2\2\34\u0081\3")
        buf.write("\2\2\2\36\u0083\3\2\2\2 \u0086\3\2\2\2\"\u008d\3\2\2\2")
        buf.write("$\u0090\3\2\2\2&\u0092\3\2\2\2(\u0095\3\2\2\2*\u0097\3")
        buf.write("\2\2\2,.\5\4\3\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3")
        buf.write("\2\2\2\60\3\3\2\2\2\61/\3\2\2\2\62\63\b\3\1\2\639\5\6")
        buf.write("\4\2\649\5\b\5\2\659\5\16\b\2\669\5\f\7\2\679\5\n\6\2")
        buf.write("8\62\3\2\2\28\64\3\2\2\28\65\3\2\2\28\66\3\2\2\28\67\3")
        buf.write("\2\2\29?\3\2\2\2:;\f\4\2\2;<\7\3\2\2<>\5\4\3\5=:\3\2\2")
        buf.write("\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\5\3\2\2\2A?\3\2\2\2")
        buf.write("BC\7\4\2\2CD\5\4\3\2DE\7\5\2\2E\7\3\2\2\2FG\7\6\2\2G\t")
        buf.write("\3\2\2\2HI\7\7\2\2IJ\5\4\3\2J\13\3\2\2\2KL\7\b\2\2LM\5")
        buf.write("\20\t\2MN\7\t\2\2NO\5\24\13\2OT\7\n\2\2PQ\7\13\2\2QR\5")
        buf.write("\32\16\2RS\5*\26\2SU\3\2\2\2TP\3\2\2\2TU\3\2\2\2UV\3\2")
        buf.write("\2\2VW\5\34\17\2W\r\3\2\2\2XY\7\32\2\2Y\17\3\2\2\2Zc\7")
        buf.write("\f\2\2[`\5\22\n\2\\]\7\r\2\2]_\5\22\n\2^\\\3\2\2\2_b\3")
        buf.write("\2\2\2`^\3\2\2\2`a\3\2\2\2ad\3\2\2\2b`\3\2\2\2c[\3\2\2")
        buf.write("\2cd\3\2\2\2de\3\2\2\2ef\7\16\2\2f\21\3\2\2\2gh\7\27\2")
        buf.write("\2h\23\3\2\2\2ir\7\4\2\2jo\5\26\f\2kl\7\r\2\2ln\5\26\f")
        buf.write("\2mk\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2ps\3\2\2\2q")
        buf.write("o\3\2\2\2rj\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\7\5\2\2u\25")
        buf.write("\3\2\2\2vy\5\30\r\2wy\5(\25\2xv\3\2\2\2xw\3\2\2\2y\27")
        buf.write("\3\2\2\2z{\7\17\2\2{\31\3\2\2\2|}\t\2\2\2}\33\3\2\2\2")
        buf.write("~\u0082\5\36\20\2\177\u0082\5 \21\2\u0080\u0082\5&\24")
        buf.write("\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2")
        buf.write("\2\u0082\35\3\2\2\2\u0083\u0084\7\20\2\2\u0084\u0085\5")
        buf.write("\4\3\2\u0085\37\3\2\2\2\u0086\u0089\5\4\3\2\u0087\u008a")
        buf.write("\5\"\22\2\u0088\u008a\5$\23\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\5\4\3\2")
        buf.write("\u008c!\3\2\2\2\u008d\u008e\7\21\2\2\u008e\u008f\5(\25")
        buf.write("\2\u008f#\3\2\2\2\u0090\u0091\7\22\2\2\u0091%\3\2\2\2")
        buf.write("\u0092\u0093\7\7\2\2\u0093\u0094\5\34\17\2\u0094\'\3\2")
        buf.write("\2\2\u0095\u0096\t\3\2\2\u0096)\3\2\2\2\u0097\u0098\t")
        buf.write("\4\2\2\u0098+\3\2\2\2\r/8?T`corx\u0081\u0089")
        return buf.getvalue()


class PRBATLFormulaParser ( Parser ):

    grammarFileName = "PRBATLFormula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'or'", "'('", "')'", "'T'", "'not'", 
                     "'<<'", "'^'", "'>>'", "'prob'", "'{'", "','", "'}'", 
                     "'*'", "'Next'", "'Until^'", "'Until'", "'<'", "'>'", 
                     "'=<'", "'>='", "<INVALID>", "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", 
                      "POSITIVE_NUMBER", "NUMBER_0", "POSITIVE_REAL_NUMBER", 
                      "NAME", "WS", "LINE_COMMENT" ]

    RULE_formulas = 0
    RULE_state_formula = 1
    RULE_enclosed_state_formula = 2
    RULE_top_state_formula = 3
    RULE_not_state_formula = 4
    RULE_atl_state_formula = 5
    RULE_proposition = 6
    RULE_agents = 7
    RULE_agent = 8
    RULE_bound = 9
    RULE_bound_number = 10
    RULE_infinite = 11
    RULE_comp_op = 12
    RULE_path_formula = 13
    RULE_next_formula = 14
    RULE_until_formula = 15
    RULE_finite_until = 16
    RULE_infinite_until = 17
    RULE_neg_path_formula = 18
    RULE_number = 19
    RULE_real_number = 20

    ruleNames =  [ "formulas", "state_formula", "enclosed_state_formula", 
                   "top_state_formula", "not_state_formula", "atl_state_formula", 
                   "proposition", "agents", "agent", "bound", "bound_number", 
                   "infinite", "comp_op", "path_formula", "next_formula", 
                   "until_formula", "finite_until", "infinite_until", "neg_path_formula", 
                   "number", "real_number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    LT_OP=17
    GT_OP=18
    LEQ_OP=19
    GEQ_OP=20
    POSITIVE_NUMBER=21
    NUMBER_0=22
    POSITIVE_REAL_NUMBER=23
    NAME=24
    WS=25
    LINE_COMMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.State_formulaContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,i)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_formulas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormulas" ):
                listener.enterFormulas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormulas" ):
                listener.exitFormulas(self)




    def formulas(self):

        localctx = PRBATLFormulaParser.FormulasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formulas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.T__1) | (1 << PRBATLFormulaParser.T__3) | (1 << PRBATLFormulaParser.T__4) | (1 << PRBATLFormulaParser.T__5) | (1 << PRBATLFormulaParser.NAME))) != 0):
                self.state = 42
                self.state_formula(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enclosed_state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Enclosed_state_formulaContext,0)


        def top_state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Top_state_formulaContext,0)


        def proposition(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.PropositionContext,0)


        def atl_state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Atl_state_formulaContext,0)


        def not_state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Not_state_formulaContext,0)


        def state_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.State_formulaContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,i)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_state_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterState_formula" ):
                listener.enterState_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitState_formula" ):
                listener.exitState_formula(self)



    def state_formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PRBATLFormulaParser.State_formulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_state_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.T__1]:
                self.state = 49
                self.enclosed_state_formula()
                pass
            elif token in [PRBATLFormulaParser.T__3]:
                self.state = 50
                self.top_state_formula()
                pass
            elif token in [PRBATLFormulaParser.NAME]:
                self.state = 51
                self.proposition()
                pass
            elif token in [PRBATLFormulaParser.T__5]:
                self.state = 52
                self.atl_state_formula()
                pass
            elif token in [PRBATLFormulaParser.T__4]:
                self.state = 53
                self.not_state_formula()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PRBATLFormulaParser.State_formulaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_state_formula)
                    self.state = 56
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 57
                    self.match(PRBATLFormulaParser.T__0)
                    self.state = 58
                    self.state_formula(3) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Enclosed_state_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_enclosed_state_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnclosed_state_formula" ):
                listener.enterEnclosed_state_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnclosed_state_formula" ):
                listener.exitEnclosed_state_formula(self)




    def enclosed_state_formula(self):

        localctx = PRBATLFormulaParser.Enclosed_state_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_enclosed_state_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(PRBATLFormulaParser.T__1)
            self.state = 65
            self.state_formula(0)
            self.state = 66
            self.match(PRBATLFormulaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Top_state_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_top_state_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop_state_formula" ):
                listener.enterTop_state_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop_state_formula" ):
                listener.exitTop_state_formula(self)




    def top_state_formula(self):

        localctx = PRBATLFormulaParser.Top_state_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_top_state_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(PRBATLFormulaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_state_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_not_state_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_state_formula" ):
                listener.enterNot_state_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_state_formula" ):
                listener.exitNot_state_formula(self)




    def not_state_formula(self):

        localctx = PRBATLFormulaParser.Not_state_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_not_state_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(PRBATLFormulaParser.T__4)
            self.state = 71
            self.state_formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atl_state_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agents(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.AgentsContext,0)


        def bound(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.BoundContext,0)


        def path_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Path_formulaContext,0)


        def comp_op(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Comp_opContext,0)


        def real_number(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Real_numberContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_atl_state_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtl_state_formula" ):
                listener.enterAtl_state_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtl_state_formula" ):
                listener.exitAtl_state_formula(self)




    def atl_state_formula(self):

        localctx = PRBATLFormulaParser.Atl_state_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atl_state_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(PRBATLFormulaParser.T__5)
            self.state = 74
            self.agents()
            self.state = 75
            self.match(PRBATLFormulaParser.T__6)
            self.state = 76
            self.bound()
            self.state = 77
            self.match(PRBATLFormulaParser.T__7)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PRBATLFormulaParser.T__8:
                self.state = 78
                self.match(PRBATLFormulaParser.T__8)
                self.state = 79
                self.comp_op()
                self.state = 80
                self.real_number()


            self.state = 84
            self.path_formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropositionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(PRBATLFormulaParser.NAME, 0)

        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_proposition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProposition" ):
                listener.enterProposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProposition" ):
                listener.exitProposition(self)




    def proposition(self):

        localctx = PRBATLFormulaParser.PropositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_proposition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PRBATLFormulaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.AgentContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.AgentContext,i)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_agents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgents" ):
                listener.enterAgents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgents" ):
                listener.exitAgents(self)




    def agents(self):

        localctx = PRBATLFormulaParser.AgentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_agents)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(PRBATLFormulaParser.T__9)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PRBATLFormulaParser.POSITIVE_NUMBER:
                self.state = 89
                self.agent()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PRBATLFormulaParser.T__10:
                    self.state = 90
                    self.match(PRBATLFormulaParser.T__10)
                    self.state = 91
                    self.agent()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 99
            self.match(PRBATLFormulaParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIVE_NUMBER(self):
            return self.getToken(PRBATLFormulaParser.POSITIVE_NUMBER, 0)

        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_agent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent" ):
                listener.enterAgent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent" ):
                listener.exitAgent(self)




    def agent(self):

        localctx = PRBATLFormulaParser.AgentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_agent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(PRBATLFormulaParser.POSITIVE_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoundContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bound_number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.Bound_numberContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.Bound_numberContext,i)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_bound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound" ):
                listener.enterBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound" ):
                listener.exitBound(self)




    def bound(self):

        localctx = PRBATLFormulaParser.BoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bound)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(PRBATLFormulaParser.T__1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.T__12) | (1 << PRBATLFormulaParser.POSITIVE_NUMBER) | (1 << PRBATLFormulaParser.NUMBER_0))) != 0):
                self.state = 104
                self.bound_number()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PRBATLFormulaParser.T__10:
                    self.state = 105
                    self.match(PRBATLFormulaParser.T__10)
                    self.state = 106
                    self.bound_number()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 114
            self.match(PRBATLFormulaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bound_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def infinite(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.InfiniteContext,0)


        def number(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.NumberContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_bound_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_number" ):
                listener.enterBound_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_number" ):
                listener.exitBound_number(self)




    def bound_number(self):

        localctx = PRBATLFormulaParser.Bound_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bound_number)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.infinite()
                pass
            elif token in [PRBATLFormulaParser.POSITIVE_NUMBER, PRBATLFormulaParser.NUMBER_0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.number()
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


    class InfiniteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_infinite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfinite" ):
                listener.enterInfinite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfinite" ):
                listener.exitInfinite(self)




    def infinite(self):

        localctx = PRBATLFormulaParser.InfiniteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_infinite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(PRBATLFormulaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT_OP(self):
            return self.getToken(PRBATLFormulaParser.LT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(PRBATLFormulaParser.LEQ_OP, 0)

        def GEQ_OP(self):
            return self.getToken(PRBATLFormulaParser.GEQ_OP, 0)

        def GT_OP(self):
            return self.getToken(PRBATLFormulaParser.GT_OP, 0)

        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_comp_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_op" ):
                listener.enterComp_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_op" ):
                listener.exitComp_op(self)




    def comp_op(self):

        localctx = PRBATLFormulaParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.LT_OP) | (1 << PRBATLFormulaParser.GT_OP) | (1 << PRBATLFormulaParser.LEQ_OP) | (1 << PRBATLFormulaParser.GEQ_OP))) != 0)):
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


    class Path_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def next_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Next_formulaContext,0)


        def until_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Until_formulaContext,0)


        def neg_path_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Neg_path_formulaContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_path_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath_formula" ):
                listener.enterPath_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath_formula" ):
                listener.exitPath_formula(self)




    def path_formula(self):

        localctx = PRBATLFormulaParser.Path_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_path_formula)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.next_formula()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.until_formula()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.neg_path_formula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_next_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext_formula" ):
                listener.enterNext_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext_formula" ):
                listener.exitNext_formula(self)




    def next_formula(self):

        localctx = PRBATLFormulaParser.Next_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_next_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(PRBATLFormulaParser.T__13)
            self.state = 130
            self.state_formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Until_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def state_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.State_formulaContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,i)


        def finite_until(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Finite_untilContext,0)


        def infinite_until(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Infinite_untilContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_until_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil_formula" ):
                listener.enterUntil_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil_formula" ):
                listener.exitUntil_formula(self)




    def until_formula(self):

        localctx = PRBATLFormulaParser.Until_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_until_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.state_formula(0)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.T__14]:
                self.state = 133
                self.finite_until()
                pass
            elif token in [PRBATLFormulaParser.T__15]:
                self.state = 134
                self.infinite_until()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self.state_formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Finite_untilContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.NumberContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_finite_until

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinite_until" ):
                listener.enterFinite_until(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinite_until" ):
                listener.exitFinite_until(self)




    def finite_until(self):

        localctx = PRBATLFormulaParser.Finite_untilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_finite_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(PRBATLFormulaParser.T__14)
            self.state = 140
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Infinite_untilContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_infinite_until

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfinite_until" ):
                listener.enterInfinite_until(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfinite_until" ):
                listener.exitInfinite_until(self)




    def infinite_until(self):

        localctx = PRBATLFormulaParser.Infinite_untilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_infinite_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(PRBATLFormulaParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neg_path_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Path_formulaContext,0)


        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_neg_path_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg_path_formula" ):
                listener.enterNeg_path_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg_path_formula" ):
                listener.exitNeg_path_formula(self)




    def neg_path_formula(self):

        localctx = PRBATLFormulaParser.Neg_path_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_neg_path_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(PRBATLFormulaParser.T__4)
            self.state = 145
            self.path_formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_0(self):
            return self.getToken(PRBATLFormulaParser.NUMBER_0, 0)

        def POSITIVE_NUMBER(self):
            return self.getToken(PRBATLFormulaParser.POSITIVE_NUMBER, 0)

        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = PRBATLFormulaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==PRBATLFormulaParser.POSITIVE_NUMBER or _la==PRBATLFormulaParser.NUMBER_0):
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


    class Real_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_0(self):
            return self.getToken(PRBATLFormulaParser.NUMBER_0, 0)

        def POSITIVE_NUMBER(self):
            return self.getToken(PRBATLFormulaParser.POSITIVE_NUMBER, 0)

        def POSITIVE_REAL_NUMBER(self):
            return self.getToken(PRBATLFormulaParser.POSITIVE_REAL_NUMBER, 0)

        def getRuleIndex(self):
            return PRBATLFormulaParser.RULE_real_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal_number" ):
                listener.enterReal_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal_number" ):
                listener.exitReal_number(self)




    def real_number(self):

        localctx = PRBATLFormulaParser.Real_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_real_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.POSITIVE_NUMBER) | (1 << PRBATLFormulaParser.NUMBER_0) | (1 << PRBATLFormulaParser.POSITIVE_REAL_NUMBER))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.state_formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def state_formula_sempred(self, localctx:State_formulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




