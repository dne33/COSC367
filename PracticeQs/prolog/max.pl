max(A,B,B):- A<B.
max(A,B,A):- B<A; B=A.
max([X], X).
max([H|T], Num):- T=[_|_], max(T, TailMax), max(H, TailMax, Num).

test_answer :-
    max([1, 2, 7, 4, 5], M),
    writeln(M).

test_answer2 :-
    max([], M),
    writeln("Max of an empty list is undefined!").