include "alldifferent.mzn";

int: n = 20; % The number of queens.

array [1..n] of var 1..n: q;

constraint alldifferent(q);
constraint alldifferent(i in 1..n)(q[i] + i);
constraint alldifferent(i in 1..n)(q[i] - i);