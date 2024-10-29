"""
Write a function, largestComponent, that takes in the adjacency list of an undirected graph.
The function should return the size (or the component itself) of the largest connected component in the graph 
""" 

def dfs(node, graph, seen, string):
    if node in seen:
        return
    
    
    seen.add(node)
    string = string + str(node) + "--"
    for neighbor in graph[node]:
        if neighbor not in seen:
            string = dfs(neighbor, graph, seen, string)
    
    return string

def largest_Component(graph):
    component = []
    seen = set()

    for node in graph:
        if node not in seen:
            
            string = dfs(node, graph, seen, "")
            component.append(string)

    return max(component, key=len)
    

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 5],
    3: [2, 4],
    4: [3 ,2]
}

print(largest_Component(graph))