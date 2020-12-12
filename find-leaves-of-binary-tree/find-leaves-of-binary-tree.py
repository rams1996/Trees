# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        def dfs(root,level,parent,dirs):
            if not root:
                return 
            if not root.left and not root.right:
                res.append(root.val)
                if dirs==1:
                    parent.left=None
                else:
                    parent.right=None
                return
            dfs(root.left,level+1,root,1)
            dfs(root.right,level+1,root,0)
        while root.left or root.right:
            res=[]
            dfs(root,0,None,-1)
            result.append(res)
        result.append([root.val])
        return result
            
            
                
        
