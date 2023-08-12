import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    Last Modified: 31 Jul 2018

    """
    ATOM = r"[a-z][a-zA-z\d_]*"
    HEAD = f"\\s*(?P<HEAD>{ATOM})\\s*"
    BODY = f"\\s*(?P<BODY>{ATOM}\\s*(,\\s*{ATOM}\\s*)*)\\s*"
    CLAUSE = f"{HEAD}(:-{BODY})?\\."
    KB = f"^({CLAUSE})*\\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [self.query]

    def is_goal(self, node):
        return len(node) == 0

    def outgoing_arcs(self, tail_node):
        arcs = []
        tail = list(tail_node)
        for clause in self.clauses:
            if clause[0] == tail[0]:
                head = tail[1:] if len(tail) > 1 else []
                for body in clause[1]:
                    head.insert(0, body)
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), 1))
        return arcs

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration  # don't change this one