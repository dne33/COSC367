preorder(leaf(X), [X]).
preorder(tree(Root, Left, Right), ListOut):-preorder().


/*Tests*/
test_answer :- preorder(leaf(a), L),
               writeln(L).
%[a]
test_answer :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).
%[a,b,c,d,e]