# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        maximumLevel=0
        levels={}
        def dfs(root,level):
            nonlocal maximumLevel
            if not root:
                return
            else:
                if level>maximumLevel:
                    maximumLevel=level
                if level not in levels:
                    levels[level]=root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)
        return levels[maximumLevel]
            
        
