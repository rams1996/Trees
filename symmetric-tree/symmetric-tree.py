# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(left,right):
            #Base
            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False
            case1=helper(left.left,right.right)
            case2=helper(left.right,right.left)
            return case1 and case2
        return helper(root.left,root.right)
        
