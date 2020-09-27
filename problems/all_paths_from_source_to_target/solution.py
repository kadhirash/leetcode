class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        ans = []
        target = len(graph) - 1
        
        
        while stack:
            path = stack.pop()
            
            if path[-1] == target:
                ans.append(path)
                
            else:
                for i in graph[path[-1]]:
                    if graph[path[-1]]:
                        stack.append(path+[i])
                
        return ans