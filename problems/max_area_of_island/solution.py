class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        maxi = 0

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    maxi = max(maxi, self.dfs(grid,row,col))
        return maxi
          
    def dfs(self,grid,row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 0
        return 1 + self.dfs(grid,row - 1, col) + self.dfs(grid,row,col + 1) + self.dfs(grid,row + 1, col) + self.dfs(grid,row, col- 1)