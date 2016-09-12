import pytest
from dijkstra import dijkstra
from graph import Graph


@pytest.fixture
def initial_graph():
    graph = {1: {2: 100, 3: 299},
             2: {},
             3: {1: 150}
             }
    g = Graph(graph)
    return g

def test_check_graph_creation(initial_graph):
    assert initial_graph == {1: 2, 3: 4}
