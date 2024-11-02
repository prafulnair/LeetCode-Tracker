"""
FIRST ATTEMPT>>> PRetty close i would say
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.right = right
#         self.left = left
        
"""

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def returnNode(node, nodeValue):
            if not node:
                return None  # Explicitly return None if the node doesn't exist

            if node.val == nodeValue:
                return node

            if nodeValue < node.val:
                return returnNode(node.left, nodeValue)  # Ensure to return the result
            else:
                return returnNode(node.right, nodeValue)  # Ensure to return the result
        
        def findAncestor(node, target, ancestors=None):
            if not node:
                return ancestors
            if ancestors is None:
                ancestors = set()
    
            # add the ancestor to the list
            ancestors.add(node.val)
            
            if node.val == target.val:
                return ancestors
            if node.val < target.val:
                findAncestor(node.right, target, ancestors)
            else:
                findAncestor(node.left, target, ancestors)
            
            return ancestors
        
        ancestorsOfP = findAncestor(root, p)
        ancestorsOfQ = findAncestor(root, q)
        
        # print(ancestorsOfP)
        # print(ancestorsOfQ)
        
        common_ancestors = ancestorsOfP.intersection(ancestorsOfQ)
        nodeValue = common_ancestors.pop()

        print(nodeValue)

        return returnNode(root, nodeValue)
"""

"""
BUT ACTUAL SOLUTION IS THIS 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start from the root and traverse the tree
        while root:
            # If both p and q are less than root, go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than root, go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # We have found the split point, so this is the LCA
            else:
                return root