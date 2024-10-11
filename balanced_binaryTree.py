# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.diff = 0
        def checkDepth(node):
            if not node:
                return 0

            leftDepth = checkDepth(node.left)
            rightDepth = checkDepth(node.right)

            if leftDepth == -1:
                return -1
            if rightDepth == -1:
                return -1

            self.diff = abs(leftDepth - rightDepth)
            if self.diff > 1:
                return -1

            return max(leftDepth, rightDepth) + 1
        
        return checkDepth(root) != -1

"""
Check MAXDEPTH OF BINARY TREE AND DIAMETER OF BINARY TREE
"""