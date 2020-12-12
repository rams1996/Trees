# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        preDict={}
        inDict={}
        for i,j in enumerate(preorder):
            preDict[j]=i
        for i,j in enumerate(inorder):
            inDict[j]=i
        def createTree(preStart,preEnd,inStart,inEnd):
            if preEnd-preStart<0:
                return None
            if (preEnd-preStart)==0:
                return TreeNode(preorder[preStart])
            root=inDict[preorder[preStart]]
            leftSize=root-inStart
            rightSize=inEnd-inStart
            inStartLeft=inStart
            inStartRight=inStart+leftSize-1
            inEndLeft=inStart+leftSize+1
            inEndRight=inStart+rightSize
            preStartLeft=1+preStart
            preStartRight=preStart+leftSize
            preEndLeft=preStart+leftSize+1
            preEndRight=preStart+rightSize
            newNode=TreeNode(preorder[preStart])
            left=createTree(preStartLeft,preStartRight,inStartLeft,inStartRight)
            right=createTree(preEndLeft,preEndRight,inEndLeft,inEndRight)
            newNode.left=left
            newNode.right=right
            return newNode
        return createTree(0,len(preorder)-1,0,len(inorder)-1)
