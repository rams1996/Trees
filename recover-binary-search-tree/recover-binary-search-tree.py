# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        
        first=None
        middle=None
        last=None
        prev=None
        def recoverBST(root):
            nonlocal first
            nonlocal middle
            nonlocal last
            nonlocal prev
            if root==None:
                return
            
            recoverBST(root.left)
            if prev and root.val<prev.val:
                if not first:
                    first=prev
                    middle=root
                else:
                    last=root
            prev=root
            recoverBST(root.right)
        recoverBST(root)
        if not last:
            middle.val,first.val=first.val,middle.val
        else:
            first.val,last.val=last.val,first.val
        """
        Do not return anything, modify root in-place instead.
        """
        
