# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        def dfs(root):
            if not root:
                return 0,0
​
            chooseleft,notchooseleft=dfs(root.left)
            chooseright,notchooseright=dfs(root.right)
            # print(root.val+notchooseleft+notchooseright,chooseleft+chooseright)
            return root.val+notchooseleft+notchooseright,max(notchooseleft+notchooseright,chooseleft+chooseright,chooseleft+notchooseright,chooseright+notchooseleft)
        return max(dfs(root))
