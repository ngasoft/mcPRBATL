from enum import Enum, auto
from mcprbatl.model import Model


class ComOp(Enum):
    LT = auto()
    LEQ = auto()
    GEQ = auto()
    GT = auto()

    @staticmethod
    def to_string(op):
        if op == ComOp.LT:
            return "<"
        elif op == ComOp.LEQ:
            return "=<"
        elif op == ComOp.GEQ:
            return ">="
        elif op == ComOp.GT:
            return ">"


class Formula:
    def __init__(self):
        raise TypeError("Not allow to create instances of Formula")

    def to_string(self, enclosed=False) -> str:
        pass

    def sat(self, model: Model) -> set:
        pass


class TopFormula(Formula):
    def __init__(self):
        pass

    def to_string(self, enclosed=False):
        s = ""
        if enclosed:
            s = "(" + s + ")"
        return s

    def sat(self, model:Model):
        return set(model.Q)


class PropositionFormula(Formula):
    def __init__(self, name: str):
        self.name = name

    def to_string(self, enclosed=False):
        s = self.name
        if enclosed:
            s = "(" + s + ")"
        return s

    def sat(self, model:Model):
        return set(model.pi[self.name])


class NegationFormula(Formula):
    def __init__(self, sub: Formula):
        self.sub = sub

    def sat(self, model:Model):
        return model.Q.difference(self.sub.sat(model))

    def to_string(self, enclosed=False):
        s = "not " + self.sub.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s


class OrFormula(Formula):
    def __init__(self, sub1: Formula, sub2: Formula):
        self.sub1 = sub1
        self.sub2 = sub2

    def sat(self, model:Model):
        return self.sub1.sat(model).union(self.sat(model))

    def to_string(self, enclosed=False):
        s = self.sub1.to_string(True) + " or " + self.sub2.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s


class PathFormula:
    def __init__(self):
        pass

    def to_string(self, enclosed=False) -> str:
        pass

    def pr_max(self, model:Model, state, agents, bound) -> float:
        pass

    def pr_min(self, model:Model, state, agents, bound) -> float:
        pass


class NextFormula(PathFormula):
    def __init__(self, sub: Formula):
        self.sub = sub

    def to_string(self, enclosed=False):
        s = "Next " + self.sub.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

    def pr_max(self, model:Model, state, agents, bound) -> float:
        maximum = -float('inf')
        proponent_moves = model.D(agents, state)
        opponents = model.all_agents().difference(agents)
        sub_sat = self.sub.sat(model)
        for p_m in proponent_moves:
            c = model.move_cost(agents, state, m)
            if model.cost_leq(c, bound):
                opponent_moves = model.D(opponents, state)
                minimum = maximum
                for o_m in opponent_moves:
                    minimum = +float('inf')
                    m = {**p_m, ** o_m}
                    m_list = [m[i] for i in range(1,model.n+1)]
                    pr = 0.0
                    for t in sub_sat:
                        pr += model.delta[state][str(m_list)][t]
                    if pr < minimum:
                        minimum = pr
                if minimum > maximum:
                    maximum = minimum
        return maximum



class UntilFormula(PathFormula):
    def __init__(self, sub1: PathFormula, sub2: PathFormula, k: int = float('inf')):
        self.k = k
        self.sub1 = sub1
        self.sub2 = sub2

    def to_string(self, enclosed=False):
        s = self.sub1.to_string(True) + " Until" + ("" if self.k==float('inf') else "^" + str(self.k)) + " " + self.sub2.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s


class NegPathFormula(PathFormula):
    def __init__(self, sub: PathFormula):
        self.sub = sub

    def to_string(self, enclosed=False):
        s = "not " + self.sub.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

class ATLFormula(Formula):
    def __init__(self, agents: set, bound: list, comp_op: ComOp, prob: float, path_formula: PathFormula):
        self.agents = agents
        self.bound = bound
        self.comp_op = comp_op
        self.prob = prob
        self.path_formula = path_formula

    def sat(self, model: Model) -> set:
        r = set()
        for q in model.Q:
            if self.comp_op == ComOp.GEQ:
                if self.path_formula.pr_max(model, q, self.agents, self.bound) >= self.prob:
                    r.add(q)
            elif self.comp_op == ComOp.GT:
                if self.path_formula.pr_max(model, q, self.agents, self.bound) > self.prob:
                    r.add(q)
            if self.comp_op == ComOp.LEQ:
                if self.path_formula.pr_min(model, q, self.agents, self.bound) <= self.prob:
                    r.add(q)
            elif self.comp_op == ComOp.LT:
                if self.path_formula.pr_min(model, q, self.agents, self.bound) < self.prob:
                    r.add(q)
        return r

    def to_string(self, enclosed=False):
        ag = "{" + ",".join([str(i) for i in self.agents]) + "}"
        bd = "^(" + ",".join([str(i) for i in self.bound]) + ")" if self.bound else ""
        pr = " pr " + ComOp.to_string(self.comp_op) + str(self.prob)
        s = "<< " + ag + bd + " >>" + pr + " " + self.path_formula.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

