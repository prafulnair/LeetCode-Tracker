# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
            
        result = 1 + max(Solution.maxDepth(self,root.left), Solution.maxDepth(self, root.right))
        return result
    
"""
Pretty straightforward solution. I had the intuition correct but for some reason I couldn't code it directly at the first short. Then I had to see where I was going wrong. I wasn't going wrong, I just 
coded it in a very convoluted, unnecessarily long way, which introduced some bugs. SO this 4 lines of code pretty much does the job. Its exactly how I imagined the solution.
You are given the root of the tree. We say, if we are at an existing root, say depth = depth + 1 and then we have to get the max length from its possible two children
The base case works out perfectly as if a root is non-existent, return zero. (That is incase one sibling is not existing, we simply get 0 from that function call)
"""
