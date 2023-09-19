listtran([], []).
listtran([Head|Tail], [TranHead|TranTail]) :- tran(Head, TranHead), listtran(Tail, TranTail).


/*Tests*/
tran(tahi,one).
tran(rua,two).
tran(toru,three).
tran(wha,four).
tran(rima,five).
tran(ono,six).
tran(whitu,seven).
tran(waru,eight).
tran(iwa,nine).

test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).
   %[tahi,whitu,ono,rua]


%tran(tahi,one).
%tran(waru,eight).

test_answer :-
    listtran([tahi], [one, eight]),
    writeln('The predicate should not succeed for lists of different lengths!').

test_answer :-
    writeln('OK').

%tran(eins,1).
%tran(zwei,2).
%tran(drei,3).
%tran(vier,4).
%tran(fuenf,5).
%tran(sechs,6).
%tran(sieben,7).
%tran(acht,8).
%tran(neun,9).

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).
%[1,9,2]