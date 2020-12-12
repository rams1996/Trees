# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        from collections import Counter
        def isPalindrome(string):
            even,odd=False,False
            if len(string)%2==0:
                even=True
            else:
                odd=True
            freq=Counter(string)
            
            for i in freq:
                if even:
                    if freq[i]%2!=0:
                        return False
            flag=True
            for i in freq:
                if odd:
                    if freq[i]%2!=0 and flag:
                        flag=False
                    elif freq[i]%2!=0 and not flag:
                        return False
            return True
        count=0
        def dfs(root,string):
            nonlocal count
            if not root:
                return
            if not root.left and not root.right:
                newStr=string+str(root.val)
                if isPalindrome(newStr):
                    count+=1
                return 
            dfs(root.left,string+str(root.val))
            dfs(root.right,string+str(root.val))
        dfs(root,"")
        return count
            
        
        
        
