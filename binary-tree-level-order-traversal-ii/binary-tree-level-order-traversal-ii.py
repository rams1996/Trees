# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while(queue):
            size=len(queue)
            level=[]
            for i in range(size):
                currNode=queue.popleft()
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(level)
        return res[::-1]
                
                
        
        
