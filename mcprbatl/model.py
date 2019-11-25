class Model:
    def __init__(self):
        self.n = 1
        self.r = 0
        self.Q = set()
        self.Pi = set()
        self.pi = dict()
        self.d = dict()
        self.c = dict()
        self.delta = dict()

    def all_agents(self):
        all = [i for i in range(1,self.n+1)]
        return set(all)

    def D(self, agents, state):
        r = set()
        m = dict()
        for a in agents:
            m[a] = 0

        while True:
            r.add(m)
            if self.last_move(agents, state, m):
                break
            m = self.next_move(agents, state, m)
        return r

    def last_move(self, agents, state, m):
        for a in agents:
            if self.d[state][a] > m:
                return False
        return True

    def next_move(self, agents, state, m):
        m = dict(m)
        for a in agents:
            if self.d[state][a] > m[a]:
                m[a] += 1
                return m
            m[a] = 0

    def move_cost(self, agents, state, m):
        c = [0,] * self.r
        for i in range(self.r):
            for a in agents:
                c[i] += self.c[state][a][m[i]]
        return tuple(c)

    def cost_leq(self, c1, c2):
        for i in range(self.r):
            if c1[i] <= c2[i]:
                pass
            else:
                return False
        return True
