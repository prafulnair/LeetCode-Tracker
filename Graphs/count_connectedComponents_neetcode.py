
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if edges == []:
            return n
        
        def generateGraph(edges):
            graph = {}

            for edge in edges:
                src, dest = edge[0], edge[1]
                if src not in graph:
                    graph[src] = []
                
                graph[src].append(dest)

                if dest not in graph:
                    graph[dest] = []
                graph[dest].append(src)

            return graph
        
        def dfs(node, graph, seen):
            if node in seen:
                return
            
            seen.add(node)
            for neighbor in graph.get(node, []):  # Use get to avoid KeyError
                if neighbor not in seen:
                    dfs(neighbor, graph, seen)

        count = 0
        seen = set()
        graph = generateGraph(edges)

        for node in range(n):  # Check all nodes from 0 to n-1
            if node not in seen:
                dfs(node, graph, seen)
                count += 1
        
        return count