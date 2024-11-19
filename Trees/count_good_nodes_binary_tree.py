# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        lastBig = float('-inf')
        def explore_dfs(node, lastBig):
            if not node:
                return 0
            
            is_good = 1 if node.val >= lastBig else 0

            newLastBig = max(lastBig, node.val)
            
            left_good = explore_dfs(node.left, newLastBig)
            right_good = explore_dfs(node.right, newLastBig)

            return is_good + left_good + right_good
 
        
        count = explore_dfs(root, lastBig)
        return count
            