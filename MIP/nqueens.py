import gurobipy as gp
from gurobipy import GRB

def start(n):
    
    # Create a new model
    m = gp.Model("nqueens")

    # Create a 2-D array of binary variables
    # x[i,j]=1 means that a queen is placed at square (i,j)
    x = m.addMVar((n, n), vtype=GRB.BINARY, name="x")

    # Add row and column constraints
    for i in range(n):

        # At most one queen per row
        m.addConstr(x[i, :].sum() == 1, name="row"+str(i))

        # At most one queen per column
        m.addConstr(x[:, i].sum() == 1, name="col"+str(i))

    for i in range(n - 1):
        diag_ru = []
        diag_lu = []
        diag_rl = []
        diag_ll = []
        for j in range(n - i):
            diag_ru += [x[i + j][j]]
            diag_lu += [x[n - 1 - (i + j)][j]]
            diag_rl += [x[i + j][n - 1 - j]]
            diag_ll += [x[n - 1 - (i + j)][n - 1 - j]]
        
    m.addConstr(sum(diag_lu) <= 1, name="diag_lu")
    m.addConstr(sum(diag_ru) <= 1, name="diag_ru")
    m.addConstr(sum(diag_ll) <= 1, name="diag_ll")
    m.addConstr(sum(diag_rl) <= 1, name="diag_rl")
    
    # Optimize model
    
    m.optimize()

    print(x.X)

start(120)