# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return None
            left=dfs(root.left)
            right=dfs(root.right)
            root.right=left
            root.left=right
            return root
        return dfs(root)
            
        
