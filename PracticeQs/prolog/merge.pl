max(A,B,A):- A>B.
max(A,B,B):- A<B; A=B.
merge([], ListB, ListB).
merge(ListA, [], ListA).
merge([HA|TA], [HB|TB], [HA|X]) :- max(HA, HB, HB), merge(TA, [HB|TB], X).
merge([HA|TA], [HB|TB], [HB|X]) :- max(HA,HB,HA), merge([HA|TA], TB, X).

test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).