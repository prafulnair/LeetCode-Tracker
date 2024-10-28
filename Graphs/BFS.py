

def breadthFirstSearch(graph, source):
    #onlyp possibly iterative
    queue = [source]

    while (queue):
        processedNode = queue.pop(0)
        print(processedNode)

        for neighbour in graph[processedNode]:
            queue.append(neighbour)





graph = {'a':['c','b'],
         'b':['d'],
         'c':['e'],
         'd':['f'],
         'e':[],
         'f':[]
         }

breadthFirstSearch(graph, 'a')