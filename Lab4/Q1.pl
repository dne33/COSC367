eats(Person, Thing) :- likes(Person, Thing).
eats(Person, Thing) :- hungry(Person), edible(Thing).
likes(bob, chocolate).
hungry(alice).

/* Test */
 test_answer :- eats(bob, chocolate), writeln('Bob eats chocolate.').