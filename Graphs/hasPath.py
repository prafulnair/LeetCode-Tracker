
"""
The Question is, given a source node and destination node in a dire ted acyclic graph
Determin if there is a path from source to destination

The idea here is to either use DFS or BFS to find the path
I also used a set 'seen' to make sure that if the neighbour is already
seen/visted once, dont try it again

The time complexity is, if n is number of nodes, e is the number of edges

Time complexity is O(n^2) or O(e)
if n is numbeer of nodes, number of edges e will be n^2

Space complexity is O(n) 
"""

def hash_pathBFS(graph, source, destination):
    if source == destination:
        return True
    seen = set()

    queue = [source]

    while(queue):
        currentNode = queue.pop(0)
        if currentNode == destination:
            return True
        seen.add(currentNode)
        for neighbour in graph[currentNode]:
            if neighbour not in seen:
                queue.append(neighbour)
    
    return False

def has_pathRecursive(graph, source, destination, seen = None):
    if not seen:
        seen = set()

    if source == destination:
        return True
    
    # if source in seen:
    #     return
    seen.add(source)
    for neighbour in graph[source]:
        if neighbour not in seen:
            if has_pathRecursive(graph, neighbour, destination, seen) == True:
                return True
    
    return False

     

def has_path(graph, source, destination):
    # we can use DFS to find if there exist a path from 
    # source to destination
    seen =set()
    stack = [source]

    while(stack):
        current = stack.pop()
        if current == destination:
            return True
        
        for neighbour in graph[current]:

            if neighbour not in seen:
                stack.append(neighbour)

    return False







# this is a acyclic graph.
graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

source = 'f'
destination = 'k'

print(has_path(graph, source, destination))
print(has_pathRecursive(graph,source,destination))
print(hash_pathBFS(graph, source, destination))
# Question is there path between soruce and destination