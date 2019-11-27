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
        agents = [i for i in range(1, self.n+1)]
        return set(agents)

    def D(self, agents, state):
        r = set()
        m = [None, ] * (self.n + 1)
        for a in agents:
            m[a] = 1

        while True:
            r.add(tuple(m))
            m = self.next_move(agents, state, m)
            if m is None:
                break

        return r

    def next_move(self, agents, state, m):
        for a in agents:
            if self.d[state][a] > m[a]:
                m[a] += 1
                return m
            m[a] = 0
        return None

    def combine_move(self, m1, m2):
        m = [None, ] * (self.n + 1)
        for a in range(1, self.n + 1):
            if m1[a] is not None:
                m[a] = m1[a]
            else:
                m[a] = m2[a]
        return tuple(m)

    def move_cost(self, agents, state, m):
        c = [0, ] * self.r
        for a in agents:
            cost = [0, ] * self.r
            if state in self.c and a in self.c[state] and m[a] in self.c[state][a]:
                cost = self.c[state][a][m[a]]
            for i in range(self.r):
                c[i] += cost[i]
        return tuple(c)

    def cost_leq(self, c1, c2):
        for i in range(self.r):
            if c1[i] <= c2[i]:
                pass
            else:
                return False
        return True

    def cost_minus(self, c1, c2):
        c = list(c1)
        for i in range(self.r):
            c[i] = c1[i] - c2[i]
        return tuple(c)

    def is_different(self, X, Y):
        for s in self.Q:
            xk = X[s].keys()
            yk = Y[s].keys()
            if xk != yk:
                return True
            for k in xk:
                if X[s][k] != Y[s][k]:
                    return True
        return False

    def is_different_k(self, k, X, Y):
        for i in range(k+1):
            for s in self.Q:
                xk = X[i][s].keys()
                yk = Y[i][s].keys()
                if xk != yk:
                    return True
                for k in xk:
                    if X[s][k] != Y[s][k]:
                        return True
        return False

    def bounds_leq(self, bound):
        b = [0 if x != float('inf') else float('inf') for x in bound]
        ret = set()
        while True:
            ret.add(tuple(b))
            b = self.next_bound(b, bound)
            if b is None:
                break
        return ret

    def next_bound(self, b, bound):
        for i in range (self.r):
            if b[i] < bound[i]:
                b[i] += 1
                return b
            elif i == self.r - 1:
                return None
            else:
                b[i] = 0

    def pr_max_min(self, state, agents, bound, sub_sat, X, min_mode=False) -> float:
        maximum = -float('inf') if not min_mode else float('inf')
        proponent_moves = self.D(agents, state)
        opponents = self.all_agents().difference(agents)
        for p_m in proponent_moves:
            c = self.move_cost(agents, state, p_m)
            if self.cost_leq(c, bound):
                bound1 = self.cost_minus(bound, c)
                opponent_moves = self.D(opponents, state)
                minimum = +float('inf') if not min_mode else -float('inf')
                for o_m in opponent_moves:
                    m = self.combine_move(p_m, o_m)
                    m_list = [m[i] for i in range(1, self.n+1)]
                    pr = 0.0
                    for t in sub_sat:
                        x = X[t][str(bound1)]
                        tran = 0.0
                        if state in self.delta and str(m_list) in self.delta[state] and t in self.delta[state][str(m_list)]:
                            tran = self.delta[state][str(m_list)][t]
                        pr += tran * x
                    if (pr < minimum and not min_mode) or (pr > minimum and min_mode):
                        minimum = pr
                if (minimum > maximum and not min_mode) or (minimum < maximum and min_mode):
                    maximum = minimum
        return maximum

    def pr_next_max_min(self, state, agents, bound, sub_sat, min_mode=False) -> float:
        maximum = -float('inf') if not min_mode else float('inf')
        proponent_moves = self.D(agents, state)
        opponents = self.all_agents().difference(agents)
        for p_m in proponent_moves:
            c = self.move_cost(agents, state, p_m)
            if self.cost_leq(c, bound):
                opponent_moves = self.D(opponents, state)
                minimum = +float('inf') if not min_mode else -float('inf')
                for o_m in opponent_moves:
                    m = self.combine_move(p_m, o_m)
                    m_list = [m[i] for i in range(1, self.n+1)]
                    pr = 0.0
                    for t in sub_sat:
                        x = 1.0
                        tran = 0.0
                        if state in self.delta and str(m_list) in self.delta[state] and t in self.delta[state][str(m_list)]:
                            tran = self.delta[state][str(m_list)][t]
                        pr += tran * x
                    if (pr < minimum and not min_mode) or (pr > minimum and min_mode):
                        minimum = pr
                if (minimum > maximum and not min_mode) or (minimum < maximum and min_mode):
                    maximum = minimum
        return maximum


