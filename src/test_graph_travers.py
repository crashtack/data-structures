# -*- coding utf-8 -*-
import pytest


GRAPH = {1: [2, 3],
         2: [],
         3: [1]}

GRAPH2 = {1: [2, 3],
          2: [4, 5],
          3: [],
          4: [],
          5: []}

TABLE = [(
    [1, 2, 3],
    [[2, 3], [], [1]]
)]


@pytest.fixture
def g():
    from graph import Graph
    GRAPH2 = {1: [2, 3],
              2: [4, 5],
              3: [],
              4: [],
              5: []}
    g = Graph(GRAPH2)
    return g


def test_graph_constructor(g):
    '''Test graph constructor if graph is passed in'''
    assert g.graph == GRAPH2


def test_dft(g):
    '''Test depth first traversal'''
    print('\n\ng: {}'.format(g.nodes()))
    assert g.depth_first_traversal(1) == [1, 2, 4, 5, 3]
