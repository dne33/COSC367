from Lab3.lab3_interpret import interpretations
from Lab3.knowledge_base import models
from Lab3.deductions import forward_deduce
from Lab3.KBGraph import KBGraph,DFSFrontier,generic_search
def main():
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
if __name__ == ("__main__"):
    main()