class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(list)
        indegrees={}
        nonTraversalGraph=defaultdict(list)
        for i in connections:
            nonTraversalGraph[i[1]].append(i[0])
            if i[0] not in indegrees:
                indegrees[i[0]]=1
            else:
                indegrees[i[0]]+=1
        
        for i in connections:
            graph[i[0]].append(i[1])
            if i[1] not in indegrees:
                indegrees[i[1]]=1
            else:
                indegrees[i[1]]+=1
        
        connectedNodes=set()
        connectedNodes.add(0)
        for i in nonTraversalGraph[0]:
            connectedNodes.add(i)
        
        needed=n-len(connectedNodes)
        from collections import deque
        queue=deque()
        queue.append(0)
        visited=set()
        visited.add(0)
        total=0
        while queue:
            currVal=queue.popleft()
            for i in nonTraversalGraph[currVal]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
            for j in graph[currVal]:
                if j not in visited:
                    visited.add(j)
                    queue.append(j)
                    total+=1
        return total
        
