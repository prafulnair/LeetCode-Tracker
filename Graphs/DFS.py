## From Free Code Camp Graph Algorithm Course

def depthFirstSearch(graph, source):
    stack = [source]
    while (stack):
        # print the top of the stack
        current = stack.pop()
        print(current)

        # push all the neightbour of the current node
        for neighbour in graph[current]:
            stack.append(neighbour)
    

def depthFirstSearchRec(graph, source):
    #print the current node/.
    print(source)

    #now call the function on neighbours
    for neighbour in graph[source]:
        depthFirstSearchRec(graph, neighbour)


graph = {'a':['b','c'],
         'b':['d'],
         'c':['e'],
         'd':['f'],
         'e':[],
         'f':[]
         }

depthFirstSearch(graph, 'a')
print("\n")
depthFirstSearchRec(graph,'a')