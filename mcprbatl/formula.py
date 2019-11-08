from antlr4 import *
from mcprbatl.parser.formula.PRBATLFormulaLexer import PRBATLFormulaLexer
from mcprbatl.parser.formula.PRBATLFormulaParser import PRBATLFormulaParser
from mcprbatl.parser.formula.PRBATLFormulaListener import PRBATLFormulaListener

from enum import Enum

ComOp = Enum("ComOp", "LT LEQ GEQ GT")


class Formula:
    def __init__(self):
        raise TypeError("Not allow to create instances of Formula")


class TopFormula(Formula):
    def __init__(self):
        pass


class PropositionFormula(Formula):
    def __init__(self, name: str):
        self.name = name


class NegationFormula(Formula):
    def __init__(self, sub: Formula):
        self.sub = sub


class OrFormula(Formula):
    def __init__(self, sub1: Formula, sub2: Formula):
        self.sub1 = sub1
        self.sub2 = sub2

class PathFormula:
    def __init__(self):
        pass


class NextFormula(PathFormula):
    def __init__(self, sub: PathFormula):
        self.sub = sub


class UntilFormula(PathFormula):
    def __init__(self, k: int, sub1: PathFormula, sub2: PathFormula):
        self.k = k
        self.sub1 = sub1
        self.sub2 = sub2

    def __init__(self, sub1: PathFormula, sub2: PathFormula):
        self.k = -1 # -1 represents infinity
        self.sub1 = sub1
        self.sub2 = sub2


class NegPathFormula(PathFormula):
    def __init__(self, sub: PathFormula):
        self.sub = sub


class ATLFormula(Formula):
    def __init__(self, agents: set, bound: list, comp_op: ComOp, prob: float, path_formula: PathFormula):
        self.agents = agents
        self.bound = bound
        self.comp_op = comp_op
        self.prob = prob
        self.path_formula = path_formula


class FormulasLoader(PRBATLFormulaListener):

    def __init__(self, file_name):
        self.file_name = file_name
        self.formulas = []
        self.cache = dict()

    def load(self):
        input_stream = FileStream(self.file_name)
        lexer = PRBATLFormulaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PRBATLFormulaParser(stream)
        tree = parser.formulas()

        walker = ParseTreeWalker()
        walker.walk(self, tree)

        return self.formulas

    def exitFormulas(self, ctx:PRBATLFormulaParser.FormulasContext):
        for ctx_f in ctx.children:
            self.formulas.append(self.cache[ctx_f])

    def exitEnclosed_state_formula(self, ctx:PRBATLFormulaParser.Enclosed_state_formulaContext):
        ctx_f = ctx.state_formula()
        ctx_p = ctx.parentCtx()
        self.cache[ctx_p] = self.cache[ctx_f]

    def exitTop_state_formula(self, ctx:PRBATLFormulaParser.Top_state_formulaContext):
        f = TopFormula()
        self.cache[ctx] = f

    def exitProposition(self, ctx:PRBATLFormulaParser.PropositionContext):
        f = PropositionFormula(ctx.NAME().getText())
        self.cache[ctx] = f

    def exitAtl_state_formula(self, ctx:PRBATLFormulaParser.Atl_state_formulaContext):
        ctx_agents = ctx.agents()
        ctx_bound = ctx.bound()
        ctx_com_op = ctx.comp_op()
        ctx_prob = ctx.real_number()
        ctx_path_formula = ctx.path_formula()

        agents = self.cache[ctx_agents]
        bound = self.cache[ctx_bound]
        ctx_com_op

    def exitAgents(self, ctx:PRBATLFormulaParser.AgentsContext):
        agents = set()
        for a in ctx:
            if isinstance(a, PRBATLFormulaParser.AgentContext):
                agents.add(int(a.POSITIVE_NUMBER().getText()))
        self.cache[ctx] = agents

    @staticmethod
    def getNumber(ctx_n):
        if ctx_n.POSITIVE_NUMBER():
            n = ctx_n.POSITIVE_NUMBER()
        else:
            n = ctx_n.NUMBER_0()
        return int(n.getText())

    def exitBound(self, ctx:PRBATLFormulaParser.BoundContext):
        bound = list()
        for b in ctx:
            if isinstance(b, PRBATLFormulaParser.Bound_numberContext):
                v = float('inf') if b.infinite() else FormulasLoader.getNumber(b.number())
                bound.append(v)
        self.cache[ctx] = bound
        
        


    def exitState_formula(self, ctx:PRBATLFormulaParser.State_formulaContext):
        pass



