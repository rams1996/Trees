# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        flag=False
        globalMax=float('-inf')
        minLessThanZero=float('-inf')
        def dfs(root):
            nonlocal flag
            nonlocal globalMax
            nonlocal minLessThanZero
            if not root:
                return 0
            if root.val<0 and root.val>minLessThanZero:
                minLessThanZero=root.val
            if not root.left and not root.right:
                if root.val>=0:
                    flag=True
                return max(0,root.val)
            
            l=dfs(root.left)
            r=dfs(root.right)
            if max(l+root.val,r+root.val)>0:
                flag=True
                globalMax=max(globalMax,l+r+root.val,l,r)
                return max(l+root.val,r+root.val)
            else:
                globalMax=max(globalMax,l,r)
                if globalMax>0:
                    flag=True
                return 0
        dfs(root)
        if flag==False:
            return minLessThanZero
        if globalMax==float('-inf'):
            return 0
