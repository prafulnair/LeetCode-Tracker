# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EXPLANATION
"""
Concept

The diameter of a binary tree is the length of the longest path between any two nodes. This path could go through the root or might be entirely in one of the subtrees.
Steps to Solve

    Use Depth to Find Paths: For each node, if you know how deep its left and right subtrees are, you can figure out the longest path that goes through that node. This is just the sum of the depths of the left and right subtrees.

    Recursive Calculation: We'll use a function that does two things: it calculates the depth of the tree and updates the longest path (diameter) found so far.

    Keep Track of the Longest Path: As we explore each node, we update a variable that keeps track of the longest path we've found.

How the Code Works

    Define a Function to Calculate Depth:
        We have a function depth(node) that returns the depth of the tree from that node down to its furthest leaf.

    Calculate Depths Recursively:
        For any given node, depth(node.left) gives the depth of the left subtree and depth(node.right) gives the depth of the right subtree.

    Update the Diameter:
        At each node, check if the sum of left_depth and right_depth is greater than the maximum diameter found so far. If it is, update the maximum diameter.

    Return the Depth:
        Each call to depth(node) returns the maximum depth of the node’s left and right children plus one (the node itself).

    Initialize and Use the Function:
        We start by calling depth(root), which initiates the recursive process starting from the root.
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDiameter = 0

        def depth(node):
            if not node:
                return 0

            leftDepth = depth(node.left)
            rightDepth = depth(node.right)

            self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)

            return max(leftDepth, rightDepth) + 1

        
        depth(root)
        return self.maxDiameter
    
    """
    543. Diameter of Binary Tree
Solved
Easy
Topics
Companies

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100


    """