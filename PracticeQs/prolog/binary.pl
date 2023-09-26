check([], 1).
check([H|T], _) :- check(T, 1), (H=0; H=1).
binary_number([0, b| X]) :- check(X, 0).

test_answer :- binary_number([0, b, 1, 0, 1]),
               writeln('OK').

test_answer1 :- binary_number([0, b, 0, 1, 2]),
               writeln('Wrong!'), halt.
test_answer1 :- writeln('OK').


test_answer2 :- binary_number([0, b]),
               writeln('Wrong'), halt.
test_answer2 :- writeln('OK').