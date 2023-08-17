directlyIn(Wrapper,Inner) :- Wrapper=olga, Inner=katarina; Wrapper=natasha, Inner=olga; Wrapper=irina, Inner=natasha.
contains(Wrapper,Inner) :- directlyIn(Inner,Wrapper); directlyIn(Z,Wrapper), contains(Z,Inner).


/* Tests*/
test_answer :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer2 :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer3 :-
    contains(katarina, irina),
    writeln('OK').
test_answer4 :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).