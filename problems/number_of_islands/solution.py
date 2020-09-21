class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs 
            # mark visited
        
        count = 0
        # edge case
        if not grid: return 0
        
        # iterate through board and perform dfs
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1': 
                    self.dfs(row,col,grid)
                    count += 1
        return count
    
    
    def dfs(self,row,col,grid):
        # validation check
        
        if row < 0 or col < 0 or row >=len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return
        
        
        # mark visited
        
        grid[row][col] = '#'
        
        
        self.dfs(row-1,col,grid)
        self.dfs(row+1,col,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row,col-1,grid)
        
        return grid
    