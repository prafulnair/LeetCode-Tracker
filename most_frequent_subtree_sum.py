# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        

        sumMap = defaultdict(int)
        def findSum(node):
            if not node:
                return 0
            
            leftSum = findSum(node.left)
            rightSum = findSum(node.right)
            total_sum = node.val + leftSum + rightSum

            sumMap[total_sum] += 1

            return total_sum
        
        findSum(root)

        maxFreq = max(sumMap.values())

        result = [s for s, freq in sumMap.items() if freq == maxFreq]
        return result
