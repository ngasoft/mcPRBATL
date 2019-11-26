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

    @staticmethod
    def reverse(op):
        if op == ComOp.LT:
            return ComOp.GT
        elif op == ComOp.LEQ:
            return ComOp.GEQ
        elif op == ComOp.GEQ:
            return ComOp.LEQ
        elif op == ComOp.GT:
            return ComOp.LT

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
        raise NotImplementedError()

    def pr_max(self, model:Model, state, agents, bound) -> float:
        raise NotImplementedError()

    def pr_min(self, model:Model, state, agents, bound) -> float:
        raise NotImplementedError()

    def pr_max_min(self, model:Model, state, agents, bound, sub_sat, X, min_mode=False) -> float:
        maximum = -float('inf') if not min_mode else float('inf')
        proponent_moves = model.D(agents, state)
        opponents = model.all_agents().difference(agents)
        for p_m in proponent_moves:
            c = model.move_cost(agents, state, p_m)
            if model.cost_leq(c, bound):
                bound1 = model.cost_minus(bound, c)
                opponent_moves = model.D(opponents, state)
                minimum = None
                for o_m in opponent_moves:
                    minimum = +float('inf') if not min_mode else -float('inf')
                    m = model.combine_move(p_m, o_m)
                    m_list = [m[i] for i in range(1, model.n+1)]
                    pr = 0.0
                    for t in sub_sat:
                        x = X[t][str(bound1)]
                        tran = 1.0
                        if state in model.delta and str(m_list) in model.delta[state] and t in model.delta[state][str(m_list)]:
                            tran = model.delta[state][str(m_list)][t]
                        pr += tran * x
                    if (pr < minimum and not min_mode) or (pr > minimum and min_mode):
                        minimum = pr
                if (minimum > maximum and not min_mode) or (minimum < maximum and min_mode):
                    maximum = minimum
        return maximum


class NextFormula(PathFormula):
    def __init__(self, sub: Formula):
        self.sub = sub

    def to_string(self, enclosed=False):
        s = "Next " + self.sub.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

    def pr_max(self, model:Model, state, agents, bound) -> float:
        X = dict()
        bounds = model.bounds_leq(bound)
        for s in model.Q:
            X[s] = dict()
            for b in bounds:
                X[s][str(b)] = 0
        sub_sat = self.sub.sat(model)
        return self.pr_max_min(model, state, agents, bound, sub_sat, X)


    def pr_min(self, model: Model, state, agents, bound) -> float:
        X = dict()
        for s in model.Q:
            X[s] = dict()
        sub_sat = self.sub.sat(model)
        return self.pr_max_min(model, state, agents, bound, X, sub_sat, True)



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

    def pr_max_inf(self, model:Model, state, agents, bound) -> float:
        X = dict()
        bounds = model.bounds_leq(bound)
        for s in model.Q:
            X[s] = dict()
            for b in bounds:
                X[s][str(b)] = 0

        while True:
            X1 = dict()
            for s in model.Q:
                X1[s] = dict()
                for b in bounds:
                    X1[s][str(b)] = self.pr_max_min(model, state, agents, bound, model.Q, X)
            if model.is_different(X1, X):
                X = X1
            else:
                break
        return X[state][str(bound)]

    def pr_min_inf(self, model:Model, state, agents, bound) -> float:
        X = dict()
        bounds = model.bounds_leq(bound)
        for s in model.Q:
            X[s] = dict()
            for b in bounds:
                X[s][str(b)] = 1

        while True:
            X1 = dict()
            for s in model.Q:
                X1[s] = dict()
                for b in bounds:
                    X1[s][str(b)] = self.pr_max_min(model, state, agents, bound, model.Q, X, True)
            if model.is_different(X1, X):
                X = X1
            else:
                break
        return X[state][str(bound)]

    def pr_max_fin(self, model:Model, state, agents, bound) -> float:
        X = [dict() for i in range(self.k+1)]
        bounds = model.bounds_leq(bound)
        for i in range(self.k + 1):
            for s in model.Q:
                X[i][s] = dict()
                for b in bounds:
                    X[i][s][str(b)] = 0

        while True:
            X1 = [dict() for i in range(self.k+1)]
            for i in range(1, self.k + 1):
                for s in model.Q:
                    X1[i][s] = dict()
                    for b in bounds:
                        X1[i][s][str(b)] = self.pr_max_min(model, state, agents, bound, model.Q, X[i-1])
            if model.is_different_k(self.k, X1, X):
                X = X1
            else:
                break
        return X[self.k][state][str(bound)]

    def pr_min_fin(self, model:Model, state, agents, bound) -> float:
        X = [dict() for i in range(1, self.k+1)]
        bounds = model.bounds_leq(bound)
        for i in range(self.k + 1):
            for s in model.Q:
                X[i][s] = dict()
                for b in bounds:
                    X[i][s][str(b)] = 1

        while True:
            X1 = [dict() for i in range(self.k + 1)]
            for i in range(self.k + 1):
                for s in model.Q:
                    X1[i][s] = dict()
                    for b in bounds:
                        X1[i][s][str(b)] = self.pr_max_min(model, state, agents, bound, model.Q, X[i], True)
            if model.is_different_k(self.k, X1, X):
                X = X1
            else:
                break
        return X[self.k][state][str(bound)]

    def pr_max(self, model:Model, state, agents, bound) -> float:
        if self.k != float('inf'):
            return self.pr_max_fin(model, state, agents, bound)
        else:
            return self.pr_max_inf(model, state, agents, bound)

    def pr_min(self, model:Model, state, agents, bound) -> float:
        if self.k != float('inf'):
            return self.pr_min_fin(model, state, agents, bound)
        else:
            return self.pr_min_inf(model, state, agents, bound)


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
        if self.path_formula is NegPathFormula:
            f = ATLFormula(self.agents, self.bound, ComOp.reverse(self.comp_op), 1-self.prob, self.path_formula.sub)
            return f.sat(model)

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

