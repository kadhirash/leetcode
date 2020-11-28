class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        row_len, col_len = len(grid), len(grid[0])
        
        count = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    count += 1
        return count
    
    
    def dfs(self,row,col,grid):
        row_len,col_len = len(grid), len(grid[0])
        
        if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != '1':
            return
        
        # mark visited
        grid[row][col] = '#'
        
        self.dfs(row+1,col,grid)
        self.dfs(row-1,col,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row,col-1,grid)