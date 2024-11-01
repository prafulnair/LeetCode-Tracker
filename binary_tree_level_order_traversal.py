# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right  
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):
            
            queue = []
            queue.append(node)
            result = []
            while(queue):
                queueLength = len(queue)
                level = []
                for _ in range(queueLength):
                    node = queue.pop(0)
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    result.append(level)
           
            return result

        return bfs(root)




            