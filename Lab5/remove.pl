remove(X, ListIn, ListIn):- \+ member(X, ListIn).
remove(X, [X | TListIn], ListOut):-  remove(X, TListIn, ListOut).
remove(X, [HListIn|TListIn], [HListIn|TListOut]):- X \= HListIn, remove(X, TListIn, TListOut).

 /*Tests*/
 test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).
%[b,c,d,b]
test_answer1 :-
    remove(2, [2], L),
    writeln(L).
%[]
test_answer2 :-
    remove(d, [a, b, c], L),
    write(L).
%[a,b,c]
test_answer3 :-
    remove(a, [], L),
    write(L).
%[]
test_answer4 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
%OK
test_answer5 :-
    \+ remove(a, [a,a,a], [a,a,a]),
    writeln('OK').
%OK