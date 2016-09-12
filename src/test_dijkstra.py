import pytest
from dijkstra import dijkstra
from graph import Graph

GRAPH1 = {1: {2: 100, 3: 299},
          2: {3: 50},
          3: {1: 150}
          }

GRAPH2 = {1: {2: 10, 3: 1, 4: 10},
          2: {5: 30},
          3: {6: 50},
          4: {5: 15, 6: 40},
          5: {7: 20},
          6: {7: 15},
          7: {},
          }


@pytest.fixture
def g():
    graph_ = Graph(GRAPH2)
    return graph_


def test_check_graph_creation(g):
    '''test that the graph is initailized properly'''
    assert g.graph == {1: {2: 100, 3: 299},
                       2: {3: 50},
                       3: {1: 150}}


def test_dijk_(g):
    '''test that dijkstra returns the shortest route'''
    assert dijkstra(g, 1, 7) == [1, 2, 3]
