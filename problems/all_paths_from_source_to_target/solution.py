class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            top_path = path[-1]
            for n in graph[top_path]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans