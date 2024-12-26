# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        
        result = []

        queue = deque([root])

        while queue:
            row_size = len(queue)
            row = []

            for _ in range(row_size):
                node = queue.popleft()
                if node: row.append(node.val)

                if node and node.left: queue.append(node.left)
                if node and node.right: queue.append(node.right)

            if row: result.append(max(row))
        
        return result