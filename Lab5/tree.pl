preorder(leaf(X), [X]).
preorder(tree(Root, Left, Right), [Root|T]):-  preorder(Left, T1), preorder(Right, T2), append(T1, T2, T).


/*Tests*/
test_answer :- preorder(leaf(a), L),
               writeln(L).
%[a]
test_answer1 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
%[a,b,c,d,e]