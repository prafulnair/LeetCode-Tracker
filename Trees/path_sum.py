# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        path = 0 

        while stack:
            node, currentSum = stack.pop()

            if not node.left and not node.right:
                if currentSum == targetSum:
                    return True
            
            if node.right:
                stack.append((node.right, currentSum+ node.right.val))
            if node.left:
                stack.append((node.left, currentSum + node.left.val))
            


        return False