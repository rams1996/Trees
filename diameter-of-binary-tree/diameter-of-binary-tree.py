# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        maxi=0
        def dfs(root):
            nonlocal maxi
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            maxi=max(maxi,left+right+1)
            return max(left,right)+1
        dfs(root)
       
        if maxi<=0:
            return 0
        return maxi-1
            
        
