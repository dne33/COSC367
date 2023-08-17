mirror(leaf(Label), leaf(Label)).
mirror(tree(L, R), tree(L2, R2)) :- mirror(L,R2), mirror(R,L2).

/*Tests*/
test_answer :-
    mirror(leaf(foo), leaf(foo)),
    write('OK').

test_answer :-
    write('Wrong answer!').


test_answer2 :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK').

test_answer2 :-
    write('Wrong answer!').


test_answer3 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  leaf(4)), T),
    write(T).

test_answer3 :-
    write('Wrong answer!').

test_answer4 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T).

test_answer4 :-
    write('Wrong answer!').