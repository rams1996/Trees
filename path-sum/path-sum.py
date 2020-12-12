# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        
        def helper(root,total):
            #Base
            if not root:
                return False
            if not root.left and not root.right and total+root.val==sum:
                return True
            #Logic
            case1=helper(root.left,total+root.val)
            case2=helper(root.right,total+root.val)
            return case1 or case2
        return helper(root,0)
        
