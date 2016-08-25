# -*- coding utf-8 -*-
import pytest

INIT_TABLE = [
    ([[12, 43], 'two', 2, {'two': 2}, ("two", 2)],
     [([12, 43], 2), ('two', 2), ('two', {'two': 2}), (("two", 2), 'two')]),
]


@pytest.mark.parametrize('init_nodes, init_edges', INIT_TABLE)
def test_graph_constructor_nodes_no_edges(init_nodes, init_edges):
    '''DOCSTRING'''
    from graph import Graph
    g = Graph(init_nodes)
    assert g.nodes == init_nodes


@pytest.mark.parametrize('init_nodes, init_edges', INIT_TABLE)
def test_graph_constructor_nodes_edges(init_nodes, init_edges):
    '''DOCSTRING'''
    from graph import Graph
    g = Graph(init_nodes, init_edges)
    assert g.nodes == init_nodes


@pytest.mark.parametrize('init_nodes, init_edges', INIT_TABLE)
def test_graph_constructor_edges(init_nodes, init_edges):
    '''DOCSTRING'''
    from graph import Graph
    g = Graph(init_nodes, init_edges)
    assert g.edges == init_edges


@pytest.mark.parametrize('init_nodes, init_edges', INIT_TABLE)
def test_graph_nodes(init_nodes, init_edges):
    '''DOCSTRING'''
    from graph import Graph
    g = Graph(init_nodes, init_edges)
    assert g.nodes == init_nodes
