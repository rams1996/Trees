# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue=deque()
        queue.append(root)
        while queue:
            currNode=queue.popleft()
            if not currNode:
                if any(queue):
                    return False
                else:
                    return True
            queue.append(currNode.left)
            queue.append(currNode.right)
        return True
            
        
