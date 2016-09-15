# -*- coding utf-8 -*-
import pytest


TABLE = [(
    [1, 2, 3],
    [{2: 100, 3: 299}, {}, {1: 150}]
)]


@pytest.fixture
def initial_graph():
    from shortest_path_graph import Graph
    graph = {1: {2: 100, 3: 299},
             2: {},
             3: {1: 150}
             }
    g = Graph(graph)
    return g


def test_node_init():
    from shortest_path_graph import Node
    n = Node(1)
    assert n.value == 1


def test_node_init_no_edges():
    from shortest_path_graph import Node
    n = Node(1)
    assert n.edges == {}


def test_node_init_distance():
    from shortest_path_graph import Node
    n = Node(1)
    assert n.distance == float('inf')


def test_node_init_no_visited():
    from shortest_path_graph import Node
    n = Node(1)
    assert n.visited is False


def test_node_edges():
    from shortest_path_graph import Node
    n = Node(1, {4: 3, 7: 90, 20: 45})
    assert n.edges == {4: 3, 7: 90, 20: 45}


def test_graph_import():
    '''Test graph constructor if graph is passed in'''
    from shortest_path_graph import Graph


def test_empty_graph():
    from shortest_path_graph import Graph
    g = Graph()
    assert g.nodes == {}


def test_constructor_with_initial_graph1(initial_graph):
    assert initial_graph.nodes[1].edges == {2: 100, 3: 299}


def test_constructor_with_initial_graph_1_visited(initial_graph):
    assert initial_graph.nodes[1].visited is False


def test_constructor_with_initial_graph_1_distance(initial_graph):
    assert initial_graph.nodes[1].distance == float('inf')


def test_constructor_with_initial_graph_2_edges(initial_graph):
    assert initial_graph.nodes[2].edges == {}


def test_constructor_with_initial_graph_2_visited(initial_graph):
    assert initial_graph.nodes[2].visited is False


def test_constructor_with_initial_graph_2_distance(initial_graph):
    assert initial_graph.nodes[2].distance == float('inf')


def test_depth_first_travers(initial_graph):
    assert initial_graph.depth_first_traversal(1) == [1, 3, 2]


def test_dijkstra(initial_graph):
    assert initial_graph.dijkstra(1, 3) == [2, 3]


# def test_graph_constructor_none():
#     '''Test graph constructor if nothing is passed in'''
#     from graph import Graph
#     g = Graph()
#     assert g.graph == {}
#
#
# @pytest.mark.parametrize('nodes_result, edges_result', TABLE)
# def test_graph_node(initial_graph, nodes_result, edges_result):
#     '''Test node returns a list of nodes'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert list(g.nodes()) == nodes_result
#
#
# def test_graph_node_no_graph():
#     '''Test node returns a list of nodes'''
#     from graph import Graph
#     g = Graph()
#     assert list(g.nodes()) == []
#
#
# @pytest.mark.parametrize('nodes_result, edges_result', TABLE)
# def test_graph_edges(initial_graph, nodes_result, edges_result):
#     '''Test node returns a list of nodes'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert list(g.edges()) == edges_result
#
#
# def test_graph_edges_no_graph():
#     '''Test node returns a list of nodes'''
#     from graph import Graph
#     g = Graph()
#     assert list(g.edges()) == []
#
#
# def test_graph_add_node(initial_graph):
#     '''Test add_node adds nodes to existing graph'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     g.add_node(4)
#     assert 4 in g
#
#
# def test_graph_add_node_empty_graph():
#     '''Test add_node adds nodes to empty graph'''
#     from graph import Graph
#     g = Graph()
#     g.add_node(4)
#     assert 4 in g
#
#
# def test_graph_add_node_duplicate(initial_graph):
#     '''Test add_node adds nodes to existing graph'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     with pytest.raises(ValueError):
#         g.add_node(3)
#
#
# def test_graph_add_edge_existing_node(initial_graph):
#     '''Test add_edge adds an edge'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     g.add_edge(2, 3, 100)
#     assert g.graph[2] == {3: 100}
#
#
# def test_graph_add_edge_new_node(initial_graph):
#     '''Test add_edge adds an edge when a new node is passed'''
#     from graph import Graph
#     # import pdb; pdb.set_trace()
#     g = Graph(initial_graph)
#     g.add_edge(5, 2, 200)
#     assert g.graph[5] == {2: 200}
#
#
# def test_graph_add_edge_new_edge_node(initial_graph):
#     '''Test add_edge adds an edge when a new node is passed as the edge'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     g.add_edge(5, 6, 150)
#     assert g.graph[6] == {}
#
#
# def test_graph_add_edge_new_node_and_new_edge_node(initial_graph):
#     '''Test add_edge adds an edge when a new node is passed as the edge'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     # import pdb; pdb.set_trace()
#     g.add_edge(6, 7, 300)
#     assert g.graph[6] == {7: 300}
#
#
# def test_graph_add_lots_of_edges(initial_graph):
#     '''Test add_edge adding lots of edges'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     # import pdb; pdb.set_trace()
#     g.add_edge(6, 7, 300)
#     g.add_edge(6, 9, 300)
#     g.add_edge(6, 1, 300)
#     g.add_edge(6, 3, 300)
#     # import pdb; pdb.set_trace()
#
#     assert g.graph[6] == {7: 300, 9: 300, 1: 300, 3: 300}
#
#
# def test_graph_del_node(initial_graph):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     g.del_node(2)
#     assert 2 not in g
#
#
# def test_graph_del_node_not_in_graph(initial_graph):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     with pytest.raises(ValueError):
#         g.del_node(5)
#
#
# def test_graph_del_node_empty_graph(initial_graph):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph()
#     with pytest.raises(ValueError):
#         g.del_node(5)
#
#
# def test_graph_del_edge(initial_graph):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     g.del_edge(1, 3)
#     assert g.graph[1] == {2: 100}
#
#
# def test_graph_del_edge_not_there(initial_graph):
#     '''Test del_node deletes a node'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     with pytest.raises(ValueError):
#         g.del_edge(6, 3)
#
#
# def test_graph_has_node_true(initial_graph):
#     '''tests has_node on a node we have'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert g.has_node(2)
#
#
# def test_graph_has_node_flase(initial_graph):
#     '''tests has_node on a node we fo not have'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert g.has_node(9) is False
#
#
# def test_graph_neighbors(initial_graph):
#     '''tests has_node on a node we have'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert g.neighbors(1) == {2: 100, 3: 299}
#
#
# def test_graph_neighbors_not_in_graph(initial_graph):
#     '''Test neighbors on node that does not exist'''
#     from graph import Graph
#     g = Graph()
#     with pytest.raises(ValueError):
#         g.neighbors(5)
#
#
# def test_graph_adjacent_true(initial_graph):
#     '''Test adjacent when values exist'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert g.adjacent(3, 1)
#
#
# def test_graph_adjacent_false(initial_graph):
#     '''Test adjacent when values exist, edge not there'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     assert g.adjacent(3, 2) == False
#
#
# def test_graph_adjacent_error(initial_graph):
#     '''Test adjacent when values do not exist'''
#     from graph import Graph
#     g = Graph(initial_graph)
#     with pytest.raises(ValueError):
#         g.adjacent(6, 5)
