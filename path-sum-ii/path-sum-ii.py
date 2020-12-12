# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result=[]
        
        
        def helper(root,total,tempList):
            tempList=list(tempList)
            #Base
            if not root:
                return 
            if not root.left and not root.right and total+root.val==sum:
                tempList.append(root.val)
                result.append(tempList)
                return
            helper(root.left,total+root.val,tempList+[root.val])
            helper(root.right,total+root.val,tempList+[root.val])
        helper(root,0,[])
        return result
                
            
        
