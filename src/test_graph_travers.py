# -*- coding utf-8 -*-
import pytest


GRAPH = {1: {2: 100, 3: 299},
             2: {},
             3: {1: 150}
             }

GRAPH2 = {1: {2: 100, 3: 299},
          2: {4: 150, 5: 250},
          3: {},
          4: {},
          5: {}
          }

TABLE = [(
    [1, 2, 3],
    [{2: 100, 3: 299}, {}, {1: 150}]
)]

GRAPHS = [
    ({1: {}}, [1], [1]),
    ({1: {2: 400}, 2: {3: 500}, 3: {1: 600}}, [1, 2, 3], [1, 2, 3])
]


@pytest.fixture(params=GRAPHS)
def g(request):
    from graph import Graph
    dict_ = request.param[0]
    graph = Graph(dict_)
    return (graph, dict_, request.param[1], request.param[2])


def test_graph_constructor(g):
    '''Test graph constructor if graph is passed in'''
    g1 = g[0]
    dict_ = g[1]
    assert g1.graph == dict_


def test_dft(g):
    '''Test depth first traversal'''
    g1 = g[0]
    dft = g[2]
    print('\n\ng: {}'.format(g1.nodes()))
    assert g1.depth_first_traversal(1) == dft


def test_bft(g):
    '''Test breadth first traversal'''
    g1 = g[0]
    bft = g[3]
    print('\n\ng: {}'.format(g1.nodes()))
    assert g1.breadth_first_traversal(1) == bft
