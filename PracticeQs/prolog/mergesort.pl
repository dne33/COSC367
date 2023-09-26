max(A,B,A):- A>B.
max(A,B,B):- A<B; A=B.
merge([], ListB, ListB).
merge(ListA, [], ListA).
merge([HA|TA], [HB|TB], [HA|X]) :- max(HA, HB, HB), merge(TA, [HB|TB], X).
merge([HA|TA], [HB|TB], [HB|X]) :- max(HA,HB,HA), merge([HA|TA], TB, X).

split_odd_even([],[],[]).
split_odd_even([H],[H],[]).
split_odd_even([H1, H2|T],[H1|TEven],[H2|TOdd]):- split_odd_even(T, TEven, TOdd).


mergesort(ListIn, Sorted) :-


test_answer :-
    merge_sort([4,3,1,2], L),
    writeln(L).