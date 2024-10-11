# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        # if the root has no children, its still symmetrical
        if not root.left and not root.right:
            return True

        dq = deque([(root.left, root.right)])

        while(dq):
            left, right = dq.popleft()
            
            # because in this case Nothing will be added to the dq and we will exit out of the loop. 
            if not left and not right:
                continue

            # in this case, one sibling is missing, which means its not symmetrical
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            dq.append([left.left, right.right])
            dq.append([left.right, right.left])

        return True


            