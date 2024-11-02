"""
FROM NEETCODE.IO
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def edgeList_to_adjList(edgeList):
            adjList = {}

            for edge in edgeList:
                source, dest = edge[0], edge[1]

                if source not in adjList: 
                    adjList[source] = []
                adjList[source].append(dest)

                if dest not in adjList:
                    adjList[dest] = []
                adjList[dest].append(source)
            
            return adjList
        
        def dfs(node, graph, seen):
            seen.add(node)
            for neighbour in graph[node]:
                if neighbour not in seen:
                    dfs(neighbour, graph, seen)
        
        if len(edges) == 0:
            return True
        graph = edgeList_to_adjList(edges)
        seen = set()
        components = 0

        for node in range(n):  # Ensure to iterate over all nodes from 0 to n-1
            if node not in seen:
                dfs(node, graph, seen)
                components += 1
        
        # A valid tree must have exactly one component and n-1 edges
        return components == 1 and len(edges) == n - 1