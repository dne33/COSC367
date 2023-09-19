solution(V1,V2,V3,H1,H2,H3) :-
    word(V1, _, I11, _, I31, _, I51, _),
    word(V2, _, I13, _, I33, _, I53, _),
    word(V3, _, I15, _, I35, _, I55, _),
    word(H1, _, I11, _, I13, _, I15, _),
    word(H2, _, I31, _, I33, _, I35, _),
    word(H3, _, I51, _, I53, _, I55, _).

/* Tests */
%word(astante, a,s,t,a,n,t,e).
%word(astoria, a,s,t,o,r,i,a).
%word(baratto, b,a,r,a,t,t,o).
%word(cobalto, c,o,b,a,l,t,o).
%word(pistola, p,i,s,t,o,l,a).
%word(statale, s,t,a,t,a,l,e).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!').

word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

test_answer2 :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer2 :- write('Wrong answer!').
