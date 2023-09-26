split_odd_even([],[],[]).
split_odd_even([H],[H],[]).
split_odd_even([H1, H2|T],[H1|TEven],[H2|TOdd]):- split_odd_even(T, TEven, TOdd).

/*Tests*/
test_answer1 :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).
%[a,c,e,g][b,d,f]
test_answer2 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).
%[1,3][2,5]
test_answer3 :-
    split_odd_even([], A, B),
    write(A),
    writeln(B).
%[][]