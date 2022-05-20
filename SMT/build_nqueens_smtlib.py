#Number of queens
n = 10 

lines = []

#Decisional Variables
lines.append("(declare-fun pos (Int) Int)")

#Domain 
lines += [f"(assert (and (>= (select pos {i}) 0) (< (select pos {i}) {n})))" for i in range(n)]

#Different columns
lines.append(f"(assert (distinct {' '.join([f'(select pos {i})' for i in range(n)])}))")

#Different Diagonals
lines.append(f"(assert (distinct {' '.join([f'(+ (select pos {i}) {i})' for i in range(n)])}))")

lines.append(f"(assert (distinct {' '.join([f'(- (select pos {i}) {i})' for i in range(n)])}))")

#Results
lines.append("(check-sat)")

lines.append(f"(get-value ({' '.join([f'(select pos {i})' for i in range(n)])}))")

with open("SMT/nqueens.smt2", "w") as f:
    for line in lines:
        f.write(line+"\n")