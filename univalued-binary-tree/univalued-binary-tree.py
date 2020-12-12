# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        treeVal=root.val
        
        def isUnivalued(root):
            #Base
            if not root:
                return True
            if root.val!=treeVal:
                return False
            #Logic
            return isUnivalued(root.left) and isUnivalued(root.right)
        return isUnivalued(root)
