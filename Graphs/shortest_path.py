"""
This function returns the shortest path between two nodes in an undirected graph using BFS.
BFS is chosen because it explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
This ensures that when we reach the destination node, it is done via the shortest possible path.
"""

def bfs_shortestPath(edges, source, destination):
    # Build the graph from the edge list
    graph = build_graph(edges)

    # Initialize the queue with the source node and a distance of 0
    queue = [(source, 0)]
    seen = set()

    # Perform BFS
    while queue:
        # Dequeue the front element
        node, distance = queue.pop(0)
        
        # Check if we've reached the destination node
        if node == destination:
            return distance  # Return the distance to the destination
        

        # Enqueue all unvisited neighbors with the updated distance
        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, distance + 1))
    
    return -1  # Return -1 if the destination is not reachable


def build_graph(edges):
    # Initialize the graph as a dictionary
    graph = {}

    # Build the graph by adding edges
    for edge in edges:
        # Ensure each edge is valid (contains exactly two nodes)
        if len(edge) != 2:
            continue
        src, dest = edge[0], edge[1]

        # Add the source node to the graph
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)  # Add the destination to the source's adjacency list

        # Add the destination node to the graph
        if dest not in graph:
            graph[dest] = []
        graph[dest].append(src)  # Add the source to the destination's adjacency list
    
    return graph  # Return the built graph


# Example usage of the functions
edges = [['w', 'x'], ['x', 'y'], ['z', 'y'], ['z', 'v'], ['w', 'v']]
graph = build_graph(edges)

# Call the BFS function to find the shortest path from 'w' to 'z'
print(bfs_shortestPath(edges, 'w', 'z'))  # Expected output: Shortest path length from 'w' to 'z'