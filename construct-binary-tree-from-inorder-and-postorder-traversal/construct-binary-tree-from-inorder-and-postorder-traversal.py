# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        # inorderLeft=0
        # inorderRight=0
        def recursion(inorder,postorder):
            # nonlocal inorderLeft
            # nonlocal inorderRight
            # print(inorder,postorder)
            if not inorder:
                return None
            if len(inorder)==1:
                return TreeNode(inorder[0])
            child=TreeNode(postorder[-1])
            for i in range(len(inorder)):
                if inorder[i]==postorder[-1]:
                    inorderLeft=inorder[0:i]
                    inorderRight=inorder[i+1:len(inorder)]
                    # print(inorderLeft,inorderRight,"SASA")
                    
            postorderLeft=postorder[0:len(inorderLeft)]
            postorderRight=postorder[len(inorderLeft):len(postorder)-1]
            # print(postorderLeft,postorderRight,"ASSAA")
            left=recursion(inorderLeft,postorderLeft)
            right=recursion(inorderRight,postorderRight)
            child.left=left
            child.right=right
            return child
        return recursion(inorder,postorder)
        
