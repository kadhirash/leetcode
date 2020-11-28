class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # build the graph
        graph = collections.defaultdict(dict) # access value that doesn't exist so no error
        for (x,y), val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1.0/val # floating point
        # dfs 
        def dfs(x,y,visited):
            # 1st condition: x,y not in graph
            if x not in graph or y not in graph:
                return -1.0
            # 2nd condition: direct connection exists
            if y in graph[x]:
                return graph[x][y]
            # 3rd condition: division but not directly connected
            for i in graph[x]: # all the nodes graph[x] is pointing to
                if i not in visited:
                    visited.add(i) 
                    temp = dfs(i,y,visited)
                    if temp == -1.0:
                        continue
                    else:
                        return graph[x][i] * temp
            # 4th condition: nothing
            return -1.0
        
        # ans 
        ans = []
        for query in queries:
            ans.append(dfs(query[0],query[1], set()))
        return ans
        