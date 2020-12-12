# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def longestZigZag(self, root):
        check = 0 # left = 1, right = 2
        count = 0
        res = 0
        
        def dfs(root,check):
            nonlocal res
            if not root:
                return None,0,check
            left,cnt1,c=dfs(root.left,1)
            right,cnt2,c=dfs(root.right,2) 
            # print(left,right,cnt1,cnt2,count,check)
            if check==0:
                if left==1:
                    a,b,c= root,max(0,cnt2+1),check
                    res=max(res,b)
                    
                if right==2:
                    a,b,c= root,max(cnt1+1,0),check
                    res=max(res,b)
                return
            elif check==1:
                a,b,c= root,max(0,cnt2+1),check
                res=max(res,b)
                return a,b,c
            elif check==2:
                a,b,c= root,max(cnt1+1,0),check
                res=max(res,b)
                return a,b,c
            
        dfs(root,0)
        return res    
                
            
            
            
            
