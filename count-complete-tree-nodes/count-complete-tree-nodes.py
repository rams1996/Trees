# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        
        def dfs(root):
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            return left+right+1
        return dfs(root)
            
        
