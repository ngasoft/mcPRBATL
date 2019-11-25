# Generated from C:/Users/ac1222/OneDrive - Coventry University/GitHub/mcPRBATL/mcprbatl/parser/grammar\PRBATLFormula.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u008c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3;\n\3\3\3\3\3\5\3?\n\3")
        buf.write("\3\3\3\3\3\3\7\3D\n\3\f\3\16\3G\13\3\3\4\3\4\3\4\3\4\7")
        buf.write("\4M\n\4\f\4\16\4P\13\4\5\4R\n\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\7\6\\\n\6\f\6\16\6_\13\6\5\6a\n\6\3\6\3\6\3")
        buf.write("\7\3\7\5\7g\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\nt\n\n\3\13\3\13\3\13\3\f\3\f\3\f\5\f|\n\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\2\3\4\22\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \2\5\3\2\13\16\3\2\27\30\3\2\27\31\2\u008b\2")
        buf.write("%\3\2\2\2\4>\3\2\2\2\6H\3\2\2\2\bU\3\2\2\2\nW\3\2\2\2")
        buf.write("\ff\3\2\2\2\16h\3\2\2\2\20j\3\2\2\2\22s\3\2\2\2\24u\3")
        buf.write("\2\2\2\26x\3\2\2\2\30\177\3\2\2\2\32\u0082\3\2\2\2\34")
        buf.write("\u0084\3\2\2\2\36\u0087\3\2\2\2 \u0089\3\2\2\2\"$\5\4")
        buf.write("\3\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2")
        buf.write("\2\2\'%\3\2\2\2()\b\3\1\2)*\7\17\2\2*+\5\4\3\2+,\7\20")
        buf.write("\2\2,?\3\2\2\2-?\7\21\2\2./\7\22\2\2/?\5\4\3\6\60?\7\32")
        buf.write("\2\2\61\62\7\25\2\2\62\63\5\6\4\2\63\64\7\3\2\2\64\65")
        buf.write("\5\n\6\2\65:\7\26\2\2\66\67\7\23\2\2\678\5\20\t\289\5")
        buf.write(" \21\29;\3\2\2\2:\66\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\5\22")
        buf.write("\n\2=?\3\2\2\2>(\3\2\2\2>-\3\2\2\2>.\3\2\2\2>\60\3\2\2")
        buf.write("\2>\61\3\2\2\2?E\3\2\2\2@A\f\4\2\2AB\7\24\2\2BD\5\4\3")
        buf.write("\5C@\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\5\3\2\2\2")
        buf.write("GE\3\2\2\2HQ\7\4\2\2IN\5\b\5\2JK\7\5\2\2KM\5\b\5\2LJ\3")
        buf.write("\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OR\3\2\2\2PN\3\2\2")
        buf.write("\2QI\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\7\6\2\2T\7\3\2\2\2")
        buf.write("UV\7\27\2\2V\t\3\2\2\2W`\7\17\2\2X]\5\f\7\2YZ\7\5\2\2")
        buf.write("Z\\\5\f\7\2[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^")
        buf.write("a\3\2\2\2_]\3\2\2\2`X\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7")
        buf.write("\20\2\2c\13\3\2\2\2dg\5\16\b\2eg\5\36\20\2fd\3\2\2\2f")
        buf.write("e\3\2\2\2g\r\3\2\2\2hi\7\7\2\2i\17\3\2\2\2jk\t\2\2\2k")
        buf.write("\21\3\2\2\2lm\7\17\2\2mn\5\22\n\2no\7\20\2\2ot\3\2\2\2")
        buf.write("pt\5\24\13\2qt\5\26\f\2rt\5\34\17\2sl\3\2\2\2sp\3\2\2")
        buf.write("\2sq\3\2\2\2sr\3\2\2\2t\23\3\2\2\2uv\7\b\2\2vw\5\4\3\2")
        buf.write("w\25\3\2\2\2x{\5\4\3\2y|\5\30\r\2z|\5\32\16\2{y\3\2\2")
        buf.write("\2{z\3\2\2\2|}\3\2\2\2}~\5\4\3\2~\27\3\2\2\2\177\u0080")
        buf.write("\7\t\2\2\u0080\u0081\5\36\20\2\u0081\31\3\2\2\2\u0082")
        buf.write("\u0083\7\n\2\2\u0083\33\3\2\2\2\u0084\u0085\7\22\2\2\u0085")
        buf.write("\u0086\5\22\n\2\u0086\35\3\2\2\2\u0087\u0088\t\3\2\2\u0088")
        buf.write("\37\3\2\2\2\u0089\u008a\t\4\2\2\u008a!\3\2\2\2\r%:>EN")
        buf.write("Q]`fs{")
        return buf.getvalue()


class PRBATLFormulaParser ( Parser ):

    grammarFileName = "PRBATLFormula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'{'", "','", "'}'", "'*'", "'Next'", 
                     "'Until^'", "'Until'", "'<'", "'>'", "'=<'", "'>='", 
                     "'('", "')'", "'T'", "'not'", "'prob'", "'or'", "'<<'", 
                     "'>>'", "<INVALID>", "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", 
                      "OPEN", "CLOSE", "TOP", "NOT", "PROB", "OR", "OPEN_AGENT", 
                      "CLOSE_AGENT", "POSITIVE_NUMBER", "NUMBER_0", "POSITIVE_REAL_NUMBER", 
                      "PROPOSITION", "NAME", "WS", "LINE_COMMENT" ]

    RULE_formulas = 0
    RULE_state_formula = 1
    RULE_agents = 2
    RULE_agent = 3
    RULE_bound = 4
    RULE_bound_number = 5
    RULE_infinite = 6
    RULE_comp_op = 7
    RULE_path_formula = 8
    RULE_next_formula = 9
    RULE_until_formula = 10
    RULE_finite_until = 11
    RULE_infinite_until = 12
    RULE_neg_path_formula = 13
    RULE_number = 14
    RULE_real_number = 15

    ruleNames =  [ "formulas", "state_formula", "agents", "agent", "bound", 
                   "bound_number", "infinite", "comp_op", "path_formula", 
                   "next_formula", "until_formula", "finite_until", "infinite_until", 
                   "neg_path_formula", "number", "real_number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    LT_OP=9
    GT_OP=10
    LEQ_OP=11
    GEQ_OP=12
    OPEN=13
    CLOSE=14
    TOP=15
    NOT=16
    PROB=17
    OR=18
    OPEN_AGENT=19
    CLOSE_AGENT=20
    POSITIVE_NUMBER=21
    NUMBER_0=22
    POSITIVE_REAL_NUMBER=23
    PROPOSITION=24
    NAME=25
    WS=26
    LINE_COMMENT=27

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.OPEN) | (1 << PRBATLFormulaParser.TOP) | (1 << PRBATLFormulaParser.NOT) | (1 << PRBATLFormulaParser.OPEN_AGENT) | (1 << PRBATLFormulaParser.PROPOSITION))) != 0):
                self.state = 32
                self.state_formula(0)
                self.state = 37
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

        def OPEN(self):
            return self.getToken(PRBATLFormulaParser.OPEN, 0)

        def state_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PRBATLFormulaParser.State_formulaContext)
            else:
                return self.getTypedRuleContext(PRBATLFormulaParser.State_formulaContext,i)


        def CLOSE(self):
            return self.getToken(PRBATLFormulaParser.CLOSE, 0)

        def TOP(self):
            return self.getToken(PRBATLFormulaParser.TOP, 0)

        def NOT(self):
            return self.getToken(PRBATLFormulaParser.NOT, 0)

        def PROPOSITION(self):
            return self.getToken(PRBATLFormulaParser.PROPOSITION, 0)

        def OPEN_AGENT(self):
            return self.getToken(PRBATLFormulaParser.OPEN_AGENT, 0)

        def agents(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.AgentsContext,0)


        def bound(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.BoundContext,0)


        def CLOSE_AGENT(self):
            return self.getToken(PRBATLFormulaParser.CLOSE_AGENT, 0)

        def path_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Path_formulaContext,0)


        def PROB(self):
            return self.getToken(PRBATLFormulaParser.PROB, 0)

        def comp_op(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Comp_opContext,0)


        def real_number(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Real_numberContext,0)


        def OR(self):
            return self.getToken(PRBATLFormulaParser.OR, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.OPEN]:
                self.state = 39
                self.match(PRBATLFormulaParser.OPEN)
                self.state = 40
                self.state_formula(0)
                self.state = 41
                self.match(PRBATLFormulaParser.CLOSE)
                pass
            elif token in [PRBATLFormulaParser.TOP]:
                self.state = 43
                self.match(PRBATLFormulaParser.TOP)
                pass
            elif token in [PRBATLFormulaParser.NOT]:
                self.state = 44
                self.match(PRBATLFormulaParser.NOT)
                self.state = 45
                self.state_formula(4)
                pass
            elif token in [PRBATLFormulaParser.PROPOSITION]:
                self.state = 46
                self.match(PRBATLFormulaParser.PROPOSITION)
                pass
            elif token in [PRBATLFormulaParser.OPEN_AGENT]:
                self.state = 47
                self.match(PRBATLFormulaParser.OPEN_AGENT)
                self.state = 48
                self.agents()
                self.state = 49
                self.match(PRBATLFormulaParser.T__0)
                self.state = 50
                self.bound()
                self.state = 51
                self.match(PRBATLFormulaParser.CLOSE_AGENT)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PRBATLFormulaParser.PROB:
                    self.state = 52
                    self.match(PRBATLFormulaParser.PROB)
                    self.state = 53
                    self.comp_op()
                    self.state = 54
                    self.real_number()


                self.state = 58
                self.path_formula()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PRBATLFormulaParser.State_formulaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_state_formula)
                    self.state = 62
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 63
                    self.match(PRBATLFormulaParser.OR)
                    self.state = 64
                    self.state_formula(3) 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_agents)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(PRBATLFormulaParser.T__1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PRBATLFormulaParser.POSITIVE_NUMBER:
                self.state = 71
                self.agent()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PRBATLFormulaParser.T__2:
                    self.state = 72
                    self.match(PRBATLFormulaParser.T__2)
                    self.state = 73
                    self.agent()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 81
            self.match(PRBATLFormulaParser.T__3)
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
        self.enterRule(localctx, 6, self.RULE_agent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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

        def OPEN(self):
            return self.getToken(PRBATLFormulaParser.OPEN, 0)

        def CLOSE(self):
            return self.getToken(PRBATLFormulaParser.CLOSE, 0)

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
        self.enterRule(localctx, 8, self.RULE_bound)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PRBATLFormulaParser.OPEN)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PRBATLFormulaParser.T__4) | (1 << PRBATLFormulaParser.POSITIVE_NUMBER) | (1 << PRBATLFormulaParser.NUMBER_0))) != 0):
                self.state = 86
                self.bound_number()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PRBATLFormulaParser.T__2:
                    self.state = 87
                    self.match(PRBATLFormulaParser.T__2)
                    self.state = 88
                    self.bound_number()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 96
            self.match(PRBATLFormulaParser.CLOSE)
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
        self.enterRule(localctx, 10, self.RULE_bound_number)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.infinite()
                pass
            elif token in [PRBATLFormulaParser.POSITIVE_NUMBER, PRBATLFormulaParser.NUMBER_0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
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
        self.enterRule(localctx, 12, self.RULE_infinite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(PRBATLFormulaParser.T__4)
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
        self.enterRule(localctx, 14, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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

        def OPEN(self):
            return self.getToken(PRBATLFormulaParser.OPEN, 0)

        def path_formula(self):
            return self.getTypedRuleContext(PRBATLFormulaParser.Path_formulaContext,0)


        def CLOSE(self):
            return self.getToken(PRBATLFormulaParser.CLOSE, 0)

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
        self.enterRule(localctx, 16, self.RULE_path_formula)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(PRBATLFormulaParser.OPEN)
                self.state = 107
                self.path_formula()
                self.state = 108
                self.match(PRBATLFormulaParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.next_formula()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.until_formula()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
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
        self.enterRule(localctx, 18, self.RULE_next_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(PRBATLFormulaParser.T__5)
            self.state = 116
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
        self.enterRule(localctx, 20, self.RULE_until_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.state_formula(0)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PRBATLFormulaParser.T__6]:
                self.state = 119
                self.finite_until()
                pass
            elif token in [PRBATLFormulaParser.T__7]:
                self.state = 120
                self.infinite_until()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
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
        self.enterRule(localctx, 22, self.RULE_finite_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(PRBATLFormulaParser.T__6)
            self.state = 126
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
        self.enterRule(localctx, 24, self.RULE_infinite_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(PRBATLFormulaParser.T__7)
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

        def NOT(self):
            return self.getToken(PRBATLFormulaParser.NOT, 0)

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
        self.enterRule(localctx, 26, self.RULE_neg_path_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(PRBATLFormulaParser.NOT)
            self.state = 131
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
        self.enterRule(localctx, 28, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
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
        self.enterRule(localctx, 30, self.RULE_real_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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
         




