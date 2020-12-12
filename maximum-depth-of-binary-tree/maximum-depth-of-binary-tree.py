# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    max=0
    def maxDepth(self, root: TreeNode) -> int:
        
        def helper(root,depth):
            #Base
            if not root:
                return 
            if not root.left and not root.right:
                if depth>self.max:
                    self.max=depth
                return
            helper(root.left,depth+1)
            helper(root.right,depth+1)
        helper(root,1)
        return self.max
                
        
