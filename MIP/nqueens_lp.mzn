int: n = 120;
array [1..n, 1..n] of var 0..1: q; 

constraint forall(i in 1..n)(sum([q[i, j] | j in 1..n]) == 1); % distinct rows
constraint forall(i in 1..n)(sum([q[j, i] | j in 1..n]) == 1); % distinct columns
constraint forall(i in 1..n-1)(sum([ q[i + j, j + 1]  | j in 0..n-i ]) <= 1); % distinct diagonals
constraint forall(i in 1..n-1)(sum([ q[n-(i+j) +1, j + 1]  | j in 0..n-i ]) <= 1); % distinct diagonals
constraint forall(i in 1..n-1)(sum([ q[i+j, n-j]  | j in 0..n-i ]) <= 1); % distinct diagonals
constraint forall(i in 1..n-1)(sum([ q[n-(i+j) + 1, n-j]  | j in 0..n-i ]) <= 1); % distinct diagonals

% search
solve satisfy;

output [ if fix(q[i, j]) == 1 then "Q" else "." endif ++
         if j == n then "\n" else "" endif | i,j in 1..n]