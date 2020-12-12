# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        h=defaultdict(list)
        def dfs(root,level):
            if not root:
                return
            if level%2==0:
                h[level].append(root.val)
            elif level%2!=0:
                h[level].insert(0,root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
            
        dfs(root,0)
        for i in h.values():
            result.append(i)
        return result
            
            
            
                
            
                    
        
