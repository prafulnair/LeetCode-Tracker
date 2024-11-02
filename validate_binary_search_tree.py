from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            # Check if current node value is within the allowable range
            if not (low < node.val < high):
                return False
            
            # Recursively validate left and right subtrees with updated ranges
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)