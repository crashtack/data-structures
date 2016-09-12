import pytest
from dijkstra import dijkstra
from graph import Graph


@pytest.fixture
def g():
    graph = {1: {2: 100, 3: 299},
             2: {3: 50},
             3: {1: 150}
             }
    graph_ = Graph(graph)
    return graph_


def test_check_graph_creation(g):
    '''test that the graph is initailized properly'''
    assert g.graph == {1: {2: 100, 3: 299},
                       2: {3: 50},
                       3: {1: 150}}


def test_dijk_(g):
    '''test that dijkstra returns the shortest route'''
    assert dijkstra(g, 1, 3) == ((1, 2, 3), 150)
