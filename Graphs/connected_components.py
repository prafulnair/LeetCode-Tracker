"""
To find out total number of connected components in forest
Write a function, connectedComponentsCount, that takes in the adjacency list 
of an undirected graph. The function should return the number of connected components 
within the graph. 

"""

def dfs(node, graph, seen):
    if node in seen:
        return
    
    seen.add(node)
    for neighbor in graph[node]:
        if neighbor not in seen:
            dfs(neighbor, graph, seen)

def countConnectedComponents(graph):
    connectedComponents = 0
    seen = set()

    for node in graph:
        if node not in seen:
            dfs(node, graph, seen)
            connectedComponents += 1  # Increment only after a full DFS for one component

    return connectedComponents



graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 5],
    3: [2, 4],
    4: [3 ,2]
}

print(countConnectedComponents(graph=graph))