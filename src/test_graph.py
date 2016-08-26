# -*- coding utf-8 -*-
import pytest


TABLE = [(
    [1, 2, 3],
    [[2, 3], [], [1]]
)]


@pytest.fixture
def initial_graph():
    graph = {1: [2, 3],
             2: [],
             3: [1]}
    return graph


def test_graph_constructor(initial_graph):
    '''Test graph constructor if graph is passed in'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.graph == initial_graph


def test_graph_constructor_none():
    '''Test graph constructor if nothing is passed in''' 
    from graph import Graph
    g = Graph()
    assert g.graph == {}


@pytest.mark.parametrize('nodes_result, edges_result', TABLE)
def test_graph_node(initial_graph, nodes_result, edges_result):
    '''Test node returns a list of nodes'''
    from graph import Graph
    g = Graph(initial_graph)
    assert list(g.nodes()) == nodes_result


def test_graph_node_no_graph():
    '''Test node returns a list of nodes'''
    from graph import Graph
    g = Graph()
    assert list(g.nodes()) == []


@pytest.mark.parametrize('nodes_result, edges_result', TABLE)
def test_graph_edges(initial_graph, nodes_result, edges_result):
    '''Test node returns a list of nodes'''
    from graph import Graph
    g = Graph(initial_graph)
    assert list(g.edges()) == edges_result


def test_graph_edges_no_graph():
    '''Test node returns a list of nodes'''
    from graph import Graph
    g = Graph()
    assert list(g.edges()) == []


def test_graph_add_node(initial_graph):
    '''Test add_node adds nodes to existing graph'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_node(4)
    assert 4 in g


def test_graph_add_node_empty_graph():
    '''Test add_node adds nodes to empty graph'''
    from graph import Graph
    g = Graph()
    g.add_node(4)
    assert 4 in g


def test_graph_add_node_duplicate(initial_graph):
    '''Test add_node adds nodes to existing graph'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.add_node(3)


def test_graph_add_edge_existing_node(initial_graph):
    '''Test add_edge adds an edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(2, 3)
    assert g.graph[2] == [3]


def test_graph_add_edge_new_node(initial_graph):
    '''Test add_edge adds an edge when a new node is passed'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(5, 2)
    assert g.graph[5] == [2]


def test_graph_add_edge_new_edge_node(initial_graph):
    '''Test add_edge adds an edge when a new node is passed as the edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(5, 6)
    assert g.graph[6] == []


def test_graph_add_edge_new_node_and_new_edge_node(initial_graph):
    '''Test add_edge adds an edge when a new node is passed as the edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(6, 7)
    assert g.graph[6] == [7]


def test_graph_del_node(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    g.del_node(2)
    assert 2 not in g


def test_graph_del_node_not_in_graph(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.del_node(5)


def test_graph_del_node_empty_graph(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph()
    with pytest.raises(ValueError):
        g.del_node(5)


def test_graph_del_edge(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    g.del_edge(1, 3)
    assert g.graph[1] == [2]


def test_graph_del_edge_not_there(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.del_edge(6, 3)


def test_graph_has_node_true(initial_graph):
    '''tests has_node on a node we have'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.has_node(2)


def test_graph_has_node_flase(initial_graph):
    '''tests has_node on a node we fo not have'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.has_node(9) == False


def test_graph_neighbors(initial_graph):
    '''tests has_node on a node we have'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.neighbors(1) == [2, 3]


def test_graph_neighbors_not_in_graph(initial_graph):
    '''Test neighbors on node that does not exist'''
    from graph import Graph
    g = Graph()
    with pytest.raises(ValueError):
        g.neighbors(5)


def test_graph_adjacent_true(initial_graph):
    '''Test adjacent when values exist'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.adjacent(3, 1)


def test_graph_adjacent_false(initial_graph):
    '''Test adjacent when values exist, edge not there'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.adjacent(3, 2) == False


def test_graph_adjacent_error(initial_graph):
    '''Test adjacent when values do not exist'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.adjacent(6, 5)


