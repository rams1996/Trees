# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while(queue):
            size=len(queue)
            add=0
            for i in range(size):
                currNode=queue.popleft()
                add=add+currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(add/size)
        return res
            
        
        
        
