class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # return min. cost so every pair there is a path of length 1 at least
        # cost = sum of connections
        # impossible = return -1
        
        def find(city):
            # Recursively re-set city's parent to its parent's parent.
            # Build the bush: ideally each tree/set is of height 1.
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parent[root2] = root1  # Always join roots!
            return True
        
        # [1] Keep track of disjoint sets. Initially each city is its own set.
        parent = {city: city for city in range(1, N+1)}
        # [2] Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:  # [3A]  
            if union(city1, city2):  # [3B]
                total += cost
        # Check that all cities are connected.
        root = find(N)
        return total if all(root == find(city) for city in range(1, N+1)) else -1