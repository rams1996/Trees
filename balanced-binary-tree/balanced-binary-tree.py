# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            if abs(l-r)>1 or l==-1 or r==-1:
                return -1
            return max(l,r)+1
        if dfs(root)==-1:
            return False
        else:
            return True
            
