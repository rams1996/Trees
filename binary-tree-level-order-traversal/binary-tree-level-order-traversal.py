# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque # O(1) remove from start or append at start
        if not root:
            return []
        queue=deque()
        
        queue.append(root)
        result=[]
        while queue:
            size=len(queue)
            temp=[]
            for i in range(size):
                currNode=queue.popleft()
                temp.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(temp)
        return result
                
        
