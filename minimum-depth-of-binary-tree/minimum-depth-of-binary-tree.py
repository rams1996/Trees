# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    min=float('inf')
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(root,minValue):
            if not root:
                return
            if not root.left and not root.right:
                if minValue<self.min:
                    self.min=minValue
                return
            helper(root.left,minValue+1)
            helper(root.right,minValue+1)
        helper(root,1)
        return self.min
    
            
        
