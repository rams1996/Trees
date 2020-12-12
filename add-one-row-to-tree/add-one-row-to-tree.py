# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        newRoot=root
        def dfs(root,leftcounter,level,parent):
            if d==1:
                nonlocal newRoot
                newRoot=TreeNode(v)
                newRoot.left=root
                return
            if level==d:
                if leftcounter==1:
                    parent.left=TreeNode(v)
                    parent.left.left=root
                    
                elif leftcounter==0:
                    parent.right=TreeNode(v)
                    parent.right.right=root
            if not root:
                return
            
            dfs(root.left,1,level+1,root)
            dfs(root.right,0,level+1,root)
        dfs(root,5,1,None)
        return newRoot
                    
                
            
            
            
            
            
            
        
            
        
        
        
        
