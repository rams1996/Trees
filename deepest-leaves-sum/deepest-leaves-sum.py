# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue=[]
        if not root:
            return queue
        queue.append(root)
        finalResult=0
        while(queue):
            size=len(queue)
            result=0
            for i in range(size):
                currNode=queue.pop(0)
                result+=currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            finalResult=result
        return finalResult
                
            
