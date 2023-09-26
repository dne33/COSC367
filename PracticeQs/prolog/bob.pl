eats(Person, Thing) :- (hungry(Person), Person='bob', edible(Thing));  (hungry(Person), Person='alice', edible(Thing), \+fast_food(Thing)).

edible(fries).
edible(salad).
fast_food(fries).

hungry(bob).
hungry(alice).


test_answer :- eats(bob, fries),
               eats(bob, salad),
               eats(alice, salad),
               write('OK').

test_answer :- write('Wrong answer!').