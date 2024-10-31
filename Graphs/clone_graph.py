
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hashmap = {}

        def dfs_to_clone(node):
            if node in hashmap:
                return hashmap[node]
            
            copy = Node(node.val) 
            hashmap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs_to_clone(neighbor))
            return copy

        if not node:
            return
        return dfs_to_clone(node)