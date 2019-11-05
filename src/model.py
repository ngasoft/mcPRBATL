class Model:
    def __init__(self, n: int, r: int, Q: set, Pi: set, pi: dict, d: dict, c: dict, sigma: dict):
        self.n = n
        self.r = r
        self.Q = Q
        self.Pi = Pi
        self.pi = pi
        self.d = d
        self.c = c
        self.sigma = sigma

    @staticmethod
    def read_from_file(fname: str):
        pass



