# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findRoot(node):
            if not node:
                return None
            if node.val == subRoot.val and verify_subtree(node, subRoot):
                return node
            
            # Recursively search in left and right subtrees
            return findRoot(node.left) or findRoot(node.right)

        
        def verify_subtree(found_root,sub_root):
            if not found_root and not sub_root:
                return True
            if not found_root or not sub_root:
                return False
            if found_root.val != sub_root.val:
                return False

            return verify_subtree(found_root.left, sub_root.left) and verify_subtree(found_root.right, sub_root.right)

        found_root = findRoot(root)
        return found_root is not None
    

"""
I almost solved this 100% on my own with my first intuition. ironically, I am doing well when it comes to
tree. 
"""