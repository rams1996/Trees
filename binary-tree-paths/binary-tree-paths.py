# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def __init__(self):
        self.res=[]
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None:
            return
        return self.recursion(root,"")
        
        
    def recursion(self,root,s):
        
        #Base Case
        if root==None:
            return
        if len(s)==0:
            s+=str(root.val)
        else:
            s+='->'+str(root.val)
        
        if root.left==None and root.right==None:
            self.res.append(s)
            return s
            
        
        
        #Logic
        self.recursion(root.left,s)
        self.recursion(root.right,s)
        return self.res
        
