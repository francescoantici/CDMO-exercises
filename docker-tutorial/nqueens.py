from z3 import *
from itertools import combinations
import time 
import json

def at_least_one(bool_vars):
    return Or(bool_vars)

def at_most_one(bool_vars):
    return [Not(And(pair[0], pair[1])) for pair in combinations(bool_vars, 2)]

def exactly_one(bool_vars):
    return at_most_one(bool_vars) + [at_least_one(bool_vars)]

def nqueens_sat(n):
    # Create all the variables
    p = [[Bool(f"x_{i}_{j}") for j in range(n)] for i in range(n)]

    # Create the solver instance
    s = Solver()

    # At least one on each row and column
    for i in range(n):
        s.add(at_least_one(p[i]))
        s.add(at_least_one([p[j][i] for j in range(n)]))

    # At most one on each row and column
    for i in range(n):
        s.add(at_most_one(p[i]))
        s.add(at_most_one([p[j][i] for j in range(n)]))

    # Add the diagonal constraints
    for i in range(n - 1):
        diag_ru_ll = []
        diag_lu_rl = []
        diag_ll_ru = []
        diag_rl_lu = []
        for j in range(n - i):
            diag_ll_ru += [p[i + j][j]]
            diag_lu_rl += [p[n - 1 - (i + j)][j]]
            diag_rl_lu += [p[i + j][n - 1 - j]]
            diag_ru_ll += [p[n - 1 - (i + j)][n - 1 - j]]
        s.add(at_most_one(diag_ru_ll))
        s.add(at_most_one(diag_lu_rl))
        s.add(at_most_one(diag_rl_lu))
        s.add(at_most_one(diag_ll_ru))
    
        # print(diag_ll, diag_lu, diag_ru, diag_rl)

    s.check()

    m = s.model()
    return [(i, j) for i in range(n) for j in range(n) if m.evaluate(p[i][j])]

if __name__ == "__main__":
    
    n = 20
    
    t0 = time.time()
    res = nqueens_sat(n)
    t1 = time.time()
    
    json_out = {
        "time" : str(t1 - t0),
        "results" : res
    }
    
    json.dump(json_out, open(f"results/z3/{n}.json", "w"),  indent = 3)