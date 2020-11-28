class Solution:
    
                    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        self.rows, self.cols = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        for row in range(self.rows):
            self.traverse(row, 0, matrix,p_visited)
            self.traverse(row, self.cols - 1, matrix,a_visited)

        for col in range(self.cols):
            self.traverse(0, col, matrix,p_visited)
            self.traverse(self.rows - 1, col, matrix,a_visited)

        return list(p_visited & a_visited)
    
    
    def traverse(self,i, j, matrix,visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        # Traverse neighbors.
        for direction in self.directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < self.rows and 0 <= next_j < self.cols:
                if matrix[next_i][next_j] >= matrix[i][j]:
                    self.traverse(next_i, next_j, matrix,visited)

    