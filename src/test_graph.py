# -*- coding utf-8 -*-
import pytest

INIT_TABLE = [
    ([[12, 43], 'two', 2, {'two': 2}, ("two", 2)],
     [([12, 43], 2), ('two', 2), ('two', {'two': 2}), (("two", 2), 'two')]),
]


@pytest.mark.parametrize('init_nodes, init_edges', INIT_TABLE)
def test_graph_constructor(init_nodes, init_edges):
    '''DOCSTRING'''
    from graph import Graph
    g = Graph(init_nodes)
    assert g.nodes == init_nodes
