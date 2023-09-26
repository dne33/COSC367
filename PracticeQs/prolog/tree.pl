postorder(leaf(X), [X]).
postorder(tree(Root, Left, Right), Traversal) :- postorder(Left, T1), postorder(Right, T2), append(T1, T2, T), append(T, [Root], Traversal).

inorder(leaf(X), [X]).
inorder(tree(Root, Left, Right), Traversal):- inorder(Left, T1), inorder(Right, T2), append(T1, [Root], LRT), append(LRT, T2, Traversal).
test_answer :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).