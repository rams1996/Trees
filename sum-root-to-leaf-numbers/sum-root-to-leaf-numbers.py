# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result=0
        def sumNums(root,result):
            #Base
            if root==None:
                return 0
            if root.left==None and root.right==None:
                return result*10+root.val
            
            #Logic
            case1=sumNums(root.left,result*10+root.val)
            case2=sumNums(root.right,result*10+root.val)
            return case1+case2
        return sumNums(root,0)
            
                    
                
                    
                    
            
            
        
        
