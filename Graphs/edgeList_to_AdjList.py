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