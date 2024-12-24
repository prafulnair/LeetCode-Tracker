# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Intuition:
        The goal is to reverse the node values at odd levels of a binary tree while
        keeping the structure intact. To achieve this, we perform a level-order 
        traversal (BFS) to process each level one by one. 

        For each odd level:
        - Extract the nodes at that level.
        - Reverse the values of the nodes in place.
        
        For BFS:
        - Use a queue to keep track of nodes at each level.
        - At each level, iterate through all nodes, enqueue their children, and 
          process the odd levels accordingly.
        
        The algorithm ensures we only modify the node values, not the structure.
        """
        from collections import deque
        
        # Initialize a queue for BFS, starting with the root
        queue = deque([root])
        level = 0  # Track the current level
        
        while queue:
            # Reverse the values of the nodes if the level is odd
            if level % 2 == 1:
                # Use two pointers to swap values of nodes at the current level
                l, r = 0, len(queue) - 1
                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val
                    l += 1
                    r -= 1
            
            # Process the current level and enqueue the children for the next level
            for _ in range(len(queue)):
                node = queue.popleft()
                
                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Increment the level counter to move to the next level
            level += 1
        
        return root