class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph={}
        def createGraph():
            for i in edges:
                if i[0] not in graph:
                    graph[i[0]]=[]
                if i[1] not in graph:
                    graph[i[1]]=[]
                graph[i[0]].append(i[-1])
                graph[i[-1]].append(i[0])
        createGraph()
        visited=set()
        dist=0
        visited=set()
        visited.add(0)
        def dfs(node):
            nonlocal dist
            if node==None:
                return 0
            c=0
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    c=c+dfs(i)
            if node==0:
                return c
            else:
                if c!=0 or hasApple[node]:
                    return c+1
                else:
                    return 0
        a=dfs(0)
        return a*2
        
                
        
