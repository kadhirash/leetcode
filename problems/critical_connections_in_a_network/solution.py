class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(previous = -1, current = 0, depth = 1):
            nonlocal depths, output
            temp_depth = depth
            depths[current] = depth
            for neighbor in graph[current]:
                if neighbor == previous:
                    continue
                neighbor_depth = depths[neighbor] or dfs(current, neighbor, depth + 1)
                if depth < neighbor_depth:
                    output.append((current, neighbor))
                elif neighbor_depth < temp_depth:
                    temp_depth = neighbor_depth
            depths[current] = temp_depth
            return temp_depth
        graph = [[] for _ in range(n)]
        depths = [0] * n
        output = []
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        dfs()
        return output