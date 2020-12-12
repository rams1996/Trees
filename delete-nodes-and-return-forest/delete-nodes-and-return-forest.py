# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        newRoot=root
        listOfHeads=[]
        def dfs(root):
            nonlocal to_delete
            if not root:
                return None
            elif not root.left and not root.right:
                return root
            leftSide=dfs(root.left)
            rightSide=dfs(root.right)
            if leftSide:
                if leftSide.val in to_delete:
                    if leftSide.right:
                        listOfHeads.append(leftSide.right)
                    if leftSide.left:
                        listOfHeads.append(leftSide.left)
                    root.left=None
                    leftSide=None
            if rightSide:
                if rightSide.val in to_delete:
                    if rightSide.right:
                        listOfHeads.append(rightSide.right)
                    if rightSide.left:
                        listOfHeads.append(rightSide.left)
                    root.right=None
                    rightSide=None
            return root
        dummy=TreeNode(-1)
        dummy.left=root
        dfs(dummy)
        if dummy.left:
            listOfHeads.append(root)
        return listOfHeads
                
                
