from graph import Graph


GRAPH = {1: {2: 100, 3: 299}, 2: {3: 50}, 3: {1: 150}}


def dijkstra(graph, start, finish):
    '''returns the shortest path between 2 nodes in a weighted graph
        and the total distance as a tuple ((1, 2, 3), 50)'''
    visited = {start: 0}
    path = {}

    nodes = set(graph.nodes())
    # import pdb; pdb.set_trace()

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for neighbor in graph.neighbors(min_node):
            # import pdb; pdb.set_trace()
            weight = current_weight + graph.neighbors(min_node)[neighbor]
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = min_node

    shortest_path = []
    for k in visited.keys():
        shortest_path.append(k)
    return visited, path, shortest_path, weight
