pair(a, t).
pair(g, c).
match(X, Y) :- pair(X,Y); pair(Y, X).
dna([], []).

dna([HA | HB], [HC|HD]) :- match(HA, HC), dna(HB, HD).

test_answer :- dna([a, t, c, g], X),
               writeln(X).

test_answer1 :- dna(X, [t, a, g, c]),
               writeln(X).