twice([],[]).
twice([Head|Tail], [X,Y|DTail]) :- twice(Tail, DTail), Head = X, Head = Y.
/*Tests*/
test_answer :-
    twice([a, b, c, d], L),
    writeln(L).
%[a,a,b,b,c,c,d,d]
test_answer1 :-
    twice(L, [1, 1, 2, 2, 3, 3]),
    writeln(L).
%[1,2,3]
test_answer2 :-
    twice([], []),
    writeln('OK').
%OK
test_answer3 :-
    twice(L1, L2),
    writeln('OK').
%OK
test_answer4 :-
    \+ twice(L, [a, a, b]),
    writeln('OK').