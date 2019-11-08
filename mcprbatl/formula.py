from enum import Enum, auto


class ComOp(Enum):
    LT = auto()
    LEQ = auto()
    GEQ = auto()
    GT = auto()


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
        self.k = float('inf')
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


