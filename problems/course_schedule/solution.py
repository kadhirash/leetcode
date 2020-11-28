class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses) ]
        visited = [ 0 for _ in range(numCourses) ]
        
        
        for x,y in prerequisites:
            graph[x].append(y)
            
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        
        # if visited, then return False
        if visited[i] == -1:
            return False
        
        # done visit, return True
        if visited[i] == 1:
            return True
        
        # mark as visited
        visited[i] = -1
        
        # visit all the neighbours
        
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
            
        # after visiting all neighbors, done visited
        visited[i] = 1
        
        return True
