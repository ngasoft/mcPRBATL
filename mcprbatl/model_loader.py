from antlr4 import *
from mcprbatl.parser.model.CGSModelLexer import CGSModelLexer
from mcprbatl.parser.model.CGSModelParser import CGSModelParser
from mcprbatl.parser.model.CGSModelListener import CGSModelListener

from mcprbatl.model import *


class ModelLoader(CGSModelListener):
    def __init__(self, file_name):
        self.file_name = file_name
        self.model = None

    def load(self):
        input_stream = FileStream(self.file_name)
        lexer = CGSModelLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CGSModelParser(stream)
        tree = parser.structure()

        self.model = Model()
        walker = ParseTreeWalker()
        walker.walk(self, tree)

        return self.model

    def enterAgents(self, ctx:CGSModelParser.AgentsContext):
        self.model.n = int(ctx.POSITIVE_NUMBER().getText())

    def exitResources(self, ctx:CGSModelParser.ResourcesContext):
        ctx_number = ctx.number()
        s = ctx_number.NUMBER_0() if ctx_number.NUMBER_0() else ctx_number.POSITIVE_NUMBER()
        self.model.r = int(s.getText())

    def exitGstates(self, ctx:CGSModelParser.GstatesContext):
        for ctx_s in ctx.children:
            if isinstance(ctx_s,CGSModelParser.GstateContext):
                self.model.Q.add(ctx_s.NAME().getText())

    def exitPropositions(self, ctx:CGSModelParser.PropositionsContext):
        for ctx_p in ctx.children:
            if isinstance(ctx_p, CGSModelParser.PropositionContext):
                self.model.Pi.add(ctx_p.NAME().getText())

    def exitLabelling(self, ctx:CGSModelParser.LabellingContext):
        ctx_proposition = ctx.proposition()
        ctx_gstates = ctx.gstates()
        states = set()
        for ctx_s in ctx_gstates.children:
            if isinstance(ctx_s, CGSModelParser.GstateContext):
                states.add(ctx_s.NAME().getText())
        self.model.pi[ctx_proposition.NAME().getText()] = states

    def exitAvailable(self, ctx:CGSModelParser.AvailableContext):
        state = ctx.gstate().NAME().getText()
        if state not in self.model.d:
            self.model.d[state] = dict()
        self.model.d[state][int(ctx.POSITIVE_NUMBER(0).getText())] = int(ctx.POSITIVE_NUMBER(1).getText())

    @staticmethod
    def getNumber(ctx_n):
        if ctx_n.POSITIVE_NUMBER():
            n = ctx_n.POSITIVE_NUMBER()
        else:
            n = ctx_n.NUMBER_0()
        return int(n.getText())

    def exitCosting(self, ctx:CGSModelParser.CostingContext):
        state = ctx.gstate().NAME().getText()
        ctx_cost = ctx.cost();
        c = [ModelLoader.getNumber(n) for n in ctx_cost.children if isinstance(n,CGSModelParser.NumberContext)]
        c = c[0:self.model.r]
        c.extend([0]*(self.model.r - len(c)))

        agent = int(ctx.POSITIVE_NUMBER(0).getText())
        action = int(ctx.POSITIVE_NUMBER(1).getText())
        if state not in self.model.c:
            self.model.c[state] = dict()
        if agent not in self.model.c[state]:
            self.model.c[state][agent] = dict()
        self.model.c[state][agent][action] = c

    def exitTransition(self, ctx:CGSModelParser.TransitionContext):
        state = ctx.gstate().NAME().getText()
        if state not in self.model.sigma:
            self.model.sigma[state] = dict()
        ctx_move:CGSModelParser.MoveContext = ctx.move()
        move = [ModelLoader.getNumber(n) for n in ctx_move.children if isinstance(n,CGSModelParser.Positive_numberContext)]
        move = move[0:self.model.n]
        move.extend([1] * (self.model.n - len(move)))

        ctx_states_distribution = ctx.states_distribution()
        dist = dict()
        sum = 0
        for ctx_state_dist in ctx_states_distribution.children:
            if isinstance(ctx_state_dist, CGSModelParser.State_distContext):
                p = float(ctx_state_dist.POSITIVE_REAL_NUMBER().getText());
                dist[ctx_state_dist.gstate().NAME().getText()] = p
                sum += p
        if sum > 0:
            for next_state in dist:
                dist[next_state] /= sum
        self.model.sigma[state][str(move)] = dist





