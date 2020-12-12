# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count=0
        def dfs(root):
            nonlocal count
            if not root.left and not root.right:
                count+=1
                return root
            if root.left:
                left=dfs(root.left)
            else:
                left=None
            if root.right:
                right=dfs(root.right)
            else:
                right=None
            if not left:
                if root.val==right.val:
                    count+=1
                    return root
                else:
                    return TreeNode(-1000)
            elif not right:
                if root.val==left.val:
                    count+=1
                    return root
                else:
                    return TreeNode(-1000)
            else:
                if root.val==left.val==right.val:
                    count+=1
                    return root
                else:
                    return TreeNode(-1000)
            
