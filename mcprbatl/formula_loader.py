#formulae loader
from antlr4 import *
from mcprbatl.parser.formula.PRBATLFormulaLexer import PRBATLFormulaLexer
from mcprbatl.parser.formula.PRBATLFormulaParser import PRBATLFormulaParser
from mcprbatl.parser.formula.PRBATLFormulaListener import PRBATLFormulaListener

from mcprbatl.formula import *


class FormulaLoader(PRBATLFormulaListener):

    def __init__(self, file_name):
        self.file_name = file_name
        self.formulas = []
        self.attachment = dict()

    def load(self):
        input_stream = FileStream(self.file_name)
        lexer = PRBATLFormulaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PRBATLFormulaParser(stream)
        tree = parser.formulas()

        walker = ParseTreeWalker()
        walker.walk(self, tree)

        return self.formulas

    def exitFormulas(self, ctx: PRBATLFormulaParser.FormulasContext):
        for ctx_f in ctx.getTypedRuleContexts(PRBATLFormulaParser.State_formulaContext):
            self.formulas.append(self.attachment[ctx_f])

    def exitAgents(self, ctx:PRBATLFormulaParser.AgentsContext):
        agents = set()
        for a in ctx.getTypedRuleContexts(PRBATLFormulaParser.AgentContext):
            agents.add(self.attachment[a])
        self.attachment[ctx] = agents

    def exitAgent(self, ctx: PRBATLFormulaParser.AgentContext):
        self.attachment[ctx] = int(ctx.POSITIVE_NUMBER().getText())

    def exitBound(self, ctx: PRBATLFormulaParser.BoundContext):
        bound = list()
        for b in ctx.getTypedRuleContexts(PRBATLFormulaParser.Bound_numberContext):
            v = self.attachment[b]
            bound.append(v)
        self.attachment[ctx] = tuple(bound)

    def exitBound_number(self, ctx: PRBATLFormulaParser.Bound_numberContext):
        if ctx.infinite():
            self.attachment[ctx] = float('inf')
        if ctx.number():
            self.attachment[ctx] = self.attachment[ctx.number()]

    def exitNumber(self, ctx: PRBATLFormulaParser.NumberContext):
        if ctx.NUMBER_0():
            self.attachment[ctx] = 0
        else:
            self.attachment[ctx] = int(ctx.POSITIVE_NUMBER().getText())

    def exitComp_op(self, ctx: PRBATLFormulaParser.Comp_opContext):
        if ctx.LT_OP():
            self.attachment[ctx] = ComOp.LT
        elif ctx.LEQ_OP():
            self.attachment[ctx] = ComOp.LEQ
        elif ctx.GT_OP():
            self.attachment[ctx] = ComOp.GT
        elif ctx.GEQ_OP():
            self.attachment[ctx] = ComOp.GEQ

    def exitReal_number(self, ctx: PRBATLFormulaParser.Real_numberContext):
        if ctx.NUMBER_0():
            self.attachment[ctx] = 0
        elif ctx.POSITIVE_NUMBER():
            self.attachment[ctx] = int(ctx.POSITIVE_NUMBER().getText())
        elif ctx.POSITIVE_REAL_NUMBER():
            self.attachment[ctx] = float(ctx.POSITIVE_REAL_NUMBER().getText())

    def exitPath_formula(self, ctx: PRBATLFormulaParser.Path_formulaContext):
        if ctx.OPEN():
            self.attachment[ctx] = self.attachment[ctx.path_formula()]
        elif ctx.next_formula():
            self.attachment[ctx] = self.attachment[ctx.next_formula()]
        elif ctx.neg_path_formula():
            self.attachment[ctx] = self.attachment[ctx.neg_path_formula()]
        elif ctx.until_formula():
            self.attachment[ctx] = self.attachment[ctx.until_formula()]

    def exitNext_formula(self, ctx: PRBATLFormulaParser.Next_formulaContext):
        self.attachment[ctx] = NextFormula(self.attachment[ctx.state_formula()])

    def exitNeg_path_formula(self, ctx: PRBATLFormulaParser.Neg_path_formulaContext):
        self.attachment[ctx] = NegPathFormula(self.attachment[ctx.path_formula()])

    def exitUntil_formula(self, ctx: PRBATLFormulaParser.Until_formulaContext):
        f1 = self.attachment[ctx.state_formula(0)]
        f2 = self.attachment[ctx.state_formula(1)]
        if ctx.finite_until():
            n = self.attachment[ctx.finite_until().number()]
            self.attachment[ctx] = UntilFormula(f1, f2, n)
        else:
            self.attachment[ctx] = UntilFormula(f1, f2)

    def exitState_formula(self, ctx: PRBATLFormulaParser.State_formulaContext):
        if ctx.OPEN():
            self.attachment[ctx] = self.attachment[ctx.state_formula(0)]
        elif ctx.TOP():
            self.attachment[ctx] = TopFormula()
        elif ctx.NOT():
            self.attachment[ctx] = NegationFormula(self.attachment[ctx.state_formula(0)])
        elif ctx.PROPOSITION():
            self.attachment[ctx] = PropositionFormula(ctx.PROPOSITION().getText())
        elif ctx.OR():
            self.attachment[ctx] = OrFormula(self.attachment[ctx.state_formula(0)], self.attachment[ctx.state_formula(1)])
        elif ctx.OPEN_AGENT():
            ctx_agents = ctx.agents()
            ctx_bound = ctx.bound()
            ctx_com_op = ctx.comp_op()
            ctx_prob = ctx.real_number()
            ctx_path_formula = ctx.path_formula()

            agents = self.attachment[ctx_agents]
            bound = self.attachment[ctx_bound]
            comp_op = ComOp.GEQ
            prob = 1.0
            if ctx_com_op and ctx_prob:
                comp_op = self.attachment[ctx_com_op]
                prob = self.attachment[ctx_prob]
            path_formula = self.attachment[ctx_path_formula]
            self.attachment[ctx] = ATLFormula(agents, bound, comp_op, prob, path_formula)
