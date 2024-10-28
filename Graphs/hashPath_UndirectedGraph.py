"""
Now we have an undirected graph with possible cycles
Is there a path between a source node and destination node in a undirected graph.

"""

def edge_list_to_adjacency_list(edge_list):
    adjacencyList = {}

    for (src, dest) in edge_list:
        if src not in adjacencyList:
            adjacencyList[src] = []
        adjacencyList[src].append(dest)

        if dest not in adjacencyList:
            adjacencyList[dest] = []
        adjacencyList[dest].append(src)


    return adjacencyList


def hasPathDFS(source, destination, graph, seen = None):

    if not seen:
        seen = set()
    
    if source == destination:
        return True
    seen.add(source)
    for neighbour in graph[source]:
        if neighbour not in seen and hasPathDFS(neighbour, destination, graph, seen) == True:
            return True
    
    return False

edge_list = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'),('i','f')]

edge_list2 = [('i','j'),('k','i'),('m','k'),('k','l'),('o','n')]
adjacency_list = edge_list_to_adjacency_list(edge_list)
adjacency_list2 = edge_list_to_adjacency_list(edge_list2)
print(adjacency_list)

source = 'a'
destination = 'f'
print(hasPathDFS(source, destination, adjacency_list))

source2 = 'j'
destination2 = 'm'

print(hasPathDFS(source2, destination2, adjacency_list2))



