# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        
        
        graph={}
        leaf=[]
        def dfs(root,prev):
            if not root:
                return None
            if not root.left and not root.right:
                leaf.append(root)
            if root.val not in graph:
                graph[root]=[]
            if prev:
                graph[root].append(prev)
            if root.left:
                graph[root].append(root.left)
            if root.right:
                graph[root].append(root.right)
            dfs(root.left,root)
            dfs(root.right,root)
            
        def dist(root,level):
            nonlocal time
            nonlocal res
            if not root or level<0:
                return
            if root in rs:
                if level<=distance:
                    res+=1
            if root not in visited:
                visited.add(root)
                for i in graph[root]:
                    dist(i,level+1)
        dfs(root,None)
        res=0
        rs=set(leaf)
        for i in range(len(leaf)):
            time=None
            visited=set()
            rs.remove(leaf[i])
            dist(leaf[i],0)
        return res
                    
                
        
