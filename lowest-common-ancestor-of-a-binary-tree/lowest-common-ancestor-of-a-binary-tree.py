# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        flag=False
        def dfs(root):
            if not root:
                return None
            if root==p:
                return p
            elif root==q:
                return q
            a=dfs(root.left)
            b=dfs(root.right)
            if a and not b:
                return a
            elif b and not a:
                return b
            elif a and b:
                return root
            else:
                return None
        return dfs(root)
                
                
        
