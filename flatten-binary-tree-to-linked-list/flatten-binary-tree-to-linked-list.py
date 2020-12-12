# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                return root
            l=dfs(root.left)
            r=dfs(root.right)
            if l:
                l.right=root.right
                root.right=root.left
                root.left=None
            return r if r else l
        return dfs(root)
        
