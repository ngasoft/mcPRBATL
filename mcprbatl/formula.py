from enum import Enum, auto
import mcprbatl

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
    state_counter = 0
    transition_counter = 0

    def __init__(self):
        raise TypeError("Not allow to create instances of Formula")

    def to_string(self, enclosed=False) -> str:
        pass

    def sat(self, model: mcprbatl.model.Model) -> set:
        pass

    def __str__(self):
        return self.to_string()


class TopFormula(Formula):
    def __init__(self):
        pass

    def to_string(self, enclosed=False):
        s = "T"
        if enclosed:
            s = "(" + s + ")"
        return s

    def sat(self, model:mcprbatl.model.Model):
        r = set(model.Q)
        Formula.state_counter += len(r)
        return r


class PropositionFormula(Formula):
    def __init__(self, name: str):
        self.name = name

    def to_string(self, enclosed=False):
        s = self.name
        if enclosed:
            s = "(" + s + ")"
        return s

    def sat(self, model:mcprbatl.model.Model):
        r = set(model.pi[self.name])
        Formula.state_counter += len(r)
        return r


class NegationFormula(Formula):
    def __init__(self, sub: Formula):
        self.sub = sub

    def sat(self, model:mcprbatl.model.Model):
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

    def sat(self, model:mcprbatl.model.Model):
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

    def __str__(self):
        return self.to_string()

    def pr_max(self, model: mcprbatl.model.Model, agents, bound):
        raise NotImplementedError()

    def pr_min(self, model: mcprbatl.model.Model, agents, bound):
        raise NotImplementedError()

    def sat_geq(self, model, agents, bound, prob: float):
        raise NotImplementedError()

    def sat_gt(self, model, agents, bound, prob: float):
        raise NotImplementedError()

    def sat_leq(self, model, agents, bound, prob: float):
        raise NotImplementedError()

    def sat_lt(self, model, agents, bound, prob: float):
        raise NotImplementedError()


class NextFormula(PathFormula):
    def __init__(self, sub: Formula):
        self.sub = sub

    def to_string(self, enclosed=False):
        s = "Next " + self.sub.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

    def pr_max(self, model: mcprbatl.model.Model, agents, bound):
        X = dict()
        sub_sat = self.sub.sat(model)
        for s in model.Q:
            X[s] = model.pr_next_max_min(s, agents, bound, sub_sat)
            Formula.state_counter += 1
        return X

    def pr_min(self, model: mcprbatl.model.Model, agents, bound):
        X = dict()
        sub_sat = self.sub.sat(model)
        for s in model.Q:
            X[s] = model.pr_next_max_min(s, agents, bound, sub_sat, True)
            Formula.state_counter += 1
        return X

    def sat_geq(self, model, agents, bound, prob: float):
        X = self.pr_max(model, agents, bound)
        ret = {q for q in model.Q if X[q] >= prob}
        return ret

    def sat_gt(self, model, agents, bound, prob: float):
        X = self.pr_max(model, agents, bound)
        ret = {q for q in model.Q if X[q] > prob}
        return ret

    def sat_lt(self, model, agents, bound, prob: float):
        X = self.pr_min(model, agents, bound)
        ret = {q for q in model.Q if X[q] < prob}
        return ret

    def sat_leq(self, model, agents, bound, prob: float):
        X = self.pr_min(model, agents, bound)
        ret = {q for q in model.Q if X[q] <= prob}
        return ret


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

    def pr_max(self, model: mcprbatl.model.Model, agents, bound):
        X = dict()
        bounds = model.bounds_leq(bound)
        sat_1 = self.sub1.sat(model)
        sat_2 = self.sub2.sat(model)
        sat_1_2 = sat_1.union(sat_2)
        for s in model.Q:
            X[s] = dict()
            for b in bounds:
                if s in sat_2:
                    X[s][str(b)] = 1.0
                elif s not in sat_1_2:
                    X[s][str(b)] = 0.0
                else:
                    X[s][str(b)] = 0.0
        t = self.k
        while t >= 0:
            X1 = dict()
            for s in model.Q:
                X1[s] = dict()
                for b in bounds:
                    if s in sat_2:
                        X1[s][str(b)] = 1.0
                    elif s not in sat_1_2:
                        X1[s][str(b)] = 0.0
                    else:
                        X1[s][str(b)] = model.pr_max_min(s, agents, b, model.Q, X)

            if model.is_different(X1, X):
                X = X1
                t -= 1
            else:
                break
        return X

    def pr_min(self, model: mcprbatl.model.Model, agents, bound):
        X = dict()
        bounds = model.bounds_leq(bound)
        sat_1 = self.sub1.sat(model)
        sat_2 = self.sub2.sat(model)
        sat_1_2 = sat_1.union(sat_2)
        for s in model.Q:
            X[s] = dict()
            for b in bounds:
                if s in sat_2:
                    X[s][str(b)] = 1.0
                elif s not in sat_1_2:
                    X[s][str(b)] = 0.0
                else:
                    X[s][str(b)] = 1.0

        t = self.k
        while t >= 0:
            X1 = dict()
            for s in model.Q:
                X1[s] = dict()
                for b in bounds:
                    if s in sat_2:
                        X1[s][str(b)] = 1.0
                    elif s not in sat_1_2:
                        X1[s][str(b)] = 0.0
                    else:
                        X1[s][str(b)] = model.pr_max_min(s, agents, b, model.Q, X, True)

            if model.is_different(X1, X):
                X = X1
                t -= 1
            else:
                break
        return X


    def sat_geq(self, model, agents, bound, prob: float):
        X = self.pr_max(model, agents, bound)
        Y = X if self.k == float('inf') else X[self.k]
        ret = {q for q in model.Q if Y[q][str(bound)] >= prob}
        Formula.state_counter += len(model.Q)
        return ret

    def sat_gt(self, model, agents, bound, prob: float):
        X = self.pr_max(model, agents, bound)
        Y = X if self.k == float('inf') else X[self.k]
        ret = {q for q in model.Q if Y[q][str(bound)] > prob}
        Formula.state_counter += len(model.Q)
        return ret

    def sat_lt(self, model, agents, bound, prob: float):
        X = self.pr_min(model, agents, bound)
        Y = X if self.k == float('inf') else X[self.k]
        ret = {q for q in model.Q if Y[q][str(bound)] < prob}
        Formula.state_counter += len(model.Q)
        return ret

    def sat_leq(self, model, agents, bound, prob: float):
        X = self.pr_min(model, agents, bound)
        Y = X if self.k == float('inf') else X[self.k]
        ret = {q for q in model.Q if Y[q][str(bound)] <= prob}
        Formula.state_counter += len(model.Q)
        return ret


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

    def sat(self, model: mcprbatl.model.Model) -> set:
        if isinstance(self.path_formula, NegPathFormula):
            f = ATLFormula(self.agents, self.bound, ComOp.reverse(self.comp_op), 1-self.prob, self.path_formula.sub)
            return f.sat(model)

        if self.comp_op == ComOp.GEQ:
            return self.path_formula.sat_geq(model, self.agents, self.bound, self.prob)
        elif self.comp_op == ComOp.GT:
            return self.path_formula.sat_gt(model, self.agents, self.bound, self.prob)
        if self.comp_op == ComOp.LEQ:
            return self.path_formula.sat_leq(model, self.agents, self.bound, self.prob)
        elif self.comp_op == ComOp.LT:
            return self.path_formula.sat_lt(model, self.agents, self.bound, self.prob)

        raise Exception("unknown comparison operator")

    def to_string(self, enclosed=False):
        ag = "{" + ",".join([str(i) for i in self.agents]) + "}"
        bd = "^(" + ",".join([str(i) for i in self.bound]) + ")" if self.bound else ""
        pr = " prob " + ComOp.to_string(self.comp_op) + " " + str(self.prob)
        s = "<< " + ag + bd + " >>" + pr + " " + self.path_formula.to_string(True)
        if enclosed:
            s = "(" + s + ")"
        return s

