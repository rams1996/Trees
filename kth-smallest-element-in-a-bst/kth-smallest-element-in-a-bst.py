# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val=-1
        def dfs(root):
            nonlocal val
            nonlocal k
            if not root:
                return 
            dfs(root.left)
            k-=1
            if k==0:
                val=root.val
            return dfs(root.right)
        dfs(root)
        return val
