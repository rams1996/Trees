# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while(queue):
            size=len(queue)
            for i in range(size):
                currNode=queue.popleft()
                if i==size-1:
                    res.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return res
                    
        
        
