# -*- coding utf-8 -*-
import pytest


TABLE = [(
    {1: [2, 3],
     2: [],
     3: [1]},
    [1, 2, 3],
    [[2, 3], [], [1]]
)]


@pytest.fixture
def initial_graph():
    graph = {1: [2, 3],
             2: [],
             3: [1]}
    return graph


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_constructor(initial_graph, nodes_result, edges_result):
    '''Test graph constructor if graph is passed in'''
    from graph import Graph
    g = Graph(initial_graph)
    assert g.graph == initial_graph


def test_graph_constructor_none():
    '''Test graph constructor if nothing is passed in''' 
    from graph import Graph
    g = Graph()
    assert g.graph == {}


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
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


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
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


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_node(initial_graph, nodes_result, edges_result):
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


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_node_duplicate(initial_graph, nodes_result, edges_result):
    '''Test add_node adds nodes to existing graph'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.add_node(3)


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_edge_existing_node(initial_graph, nodes_result, edges_result):
    '''Test add_edge adds an edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(2, 3)
    assert g.graph[2] == [3]


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_edge_new_node(initial_graph, nodes_result, edges_result):
    '''Test add_edge adds an edge when a new node is passed'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(5, 2)
    assert g.graph[5] == [2]


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_edge_new_edge_node(initial_graph, nodes_result, edges_result):
    '''Test add_edge adds an edge when a new node is passed as the edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(5, 6)
    assert g.graph[6] == []


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_add_edge_new_node_and_new_edge_node(initial_graph, nodes_result, edges_result):
    '''Test add_edge adds an edge when a new node is passed as the edge'''
    from graph import Graph
    g = Graph(initial_graph)
    g.add_edge(6, 7)
    assert g.graph[6] == [7]


@pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_del_node(initial_graph, nodes_result, edges_result):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    g.del_node(2)
    assert 2 not in g


# @pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
def test_graph_del_node_not_in_graph(initial_graph):
    '''Test del_node deletes a node'''
    from graph import Graph
    g = Graph(initial_graph)
    with pytest.raises(ValueError):
        g.del_node(5)


# @pytest.mark.parametrize('initial_graph, nodes_result, edges_result', TABLE)
# def test_graph_del_node_not_in_graph(initial_graph, nodes_result, edges_result):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     with pytest.raises(KeyError):
#         g.del_node(5)
