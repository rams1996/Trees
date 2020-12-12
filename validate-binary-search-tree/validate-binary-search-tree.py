# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(root,minimum,maximum):
            if not root:
                return True
            if root.val>=maximum or root.val<=minimum:
                return False
                
            left=dfs(root.left,minimum,root.val)
            right=dfs(root.right,root.val,maximum)
            return left and right
        abc=dfs(root,float('-inf'),float('inf'))
        return abc
            
            
        
