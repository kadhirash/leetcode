class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       # bfs
    
        if not grid or not grid[0]: return 0
        
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(i,j,grid)
                    count += 1
        return count
    
    def bfs(self,i,j,grid):
        if i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1': return 
        
        queue = collections.deque()
        queue.append((i,j))
        
        grid[i][j] = '#'
        
        while queue:
            (i,j) = queue.pop()
            
            if i-1 >= 0 and grid[i-1][j] == '1':
                queue.append((i-1,j))
                grid[i-1][j] = '0'
        
            if i+1 < len(grid) and grid[i+1][j] == '1':
                queue.append((i+1,j))
                grid[i+1][j] = '0'
                
            if j-1 >= 0 and grid[i][j-1] == '1':
                queue.append((i,j-1))
                grid[i][j-1] = '0'
                
            if j+1 < len(grid[0]) and grid[i][j+1] == '1':
                queue.append((i,j+1))
                grid[i][j+1] = '0'
        