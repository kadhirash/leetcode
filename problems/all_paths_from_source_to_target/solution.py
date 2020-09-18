class Solution:
    
    def dfs(self, curr_node, path):
        if curr_node == self.N:
            self.res.append(path)
        else:
            for i in self.graph[curr_node]:
                self.dfs(i, path + [i])
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.N = len(graph)- 1
        self.graph = graph
        self.res = []
        self.dfs(0, [0])
        return self.res
        