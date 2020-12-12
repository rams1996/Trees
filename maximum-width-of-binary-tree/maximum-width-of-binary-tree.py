# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        left={}
        maxVal=0
        right=defaultdict(list)
        def dfs(root,level,coordinate):
            if not root:
                return
            if level not in left:
                left[level]=coordinate
            right[level]=coordinate
            dfs(root.left,level+1,coordinate*2)
            dfs(root.right,level+1,coordinate*2+1)
        dfs(root,1,1)
        for i in left.keys():
            maxVal=max(maxVal,abs(left[i]-right[i])+1)
        return maxVal
            
            
            
            
            
            
            
        
