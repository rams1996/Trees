# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        depth=0
        xLevel=-1
        yLevel=-1
        xParent=None
        yParent=None
        queue=deque()
        queue.append(root)
        while(queue):
            size=len(queue)
            for i in range(size):
                currNode=queue.popleft()
                if currNode.left:
                    if currNode.left.val==x:
                        xLevel=depth
                        xParent=currNode
                    if currNode.left.val==y:
                        yLevel=depth
                        yParent=currNode
                    queue.append(currNode.left)
                    
                if currNode.right:
                    if currNode.right.val==x:
                        xParent=currNode
                        xLevel=depth
                    if currNode.right.val==y:
                        yParent=currNode
                        yLevel=depth
                    queue.append(currNode.right)
            depth+=1
        return xParent!=yParent and xLevel==yLevel
            
        
        
