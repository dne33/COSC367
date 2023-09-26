unique([], []).
unique([H|T], [H|Set]) :-  (\+member(H,T), unique(T, Set)).
unique([H|T], Set):- (member(H,T), unique(T, Set)).
test_answer :-
    unique([1,2,1,4,3,3], Set),
    sort(Set,Sorted),
    writeln(Sorted).