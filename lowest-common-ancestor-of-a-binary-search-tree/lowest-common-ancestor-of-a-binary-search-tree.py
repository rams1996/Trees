# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal=min(p.val,q.val)
        maxVal=max(p.val,q.val)
        def dfs(root):
            if not root:
                return None
            if  maxVal>=root.val and minVal<=root.val:
                return root
            elif maxVal>root.val and minVal>root.val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        return dfs(root)
        return None
        
        
        
