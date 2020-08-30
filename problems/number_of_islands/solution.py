import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]: return 0
#         # dfs
#         row_len, col_len, count = len(grid), len(grid[0]), 0
#         for row in range(row_len):
#             for col in range(col_len):
#                 if grid[row][col] == '1':
#                     self.dfs(grid,row,col)
#                     count += 1
#         return count
    
#     def dfs(self, grid, row, col):
#         row_len, col_len = len(grid), len(grid[0])
#         if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != '1': return
        
#         #mark visited
#         grid[row][col] = '$'
#         self.dfs(grid,row+1,col)
#         self.dfs(grid,row-1,col)
#         self.dfs(grid,row,col+1)
#         self.dfs(grid,row,col-1)

        if not grid or not grid[0]: return 0
        # bfs
        row_len, col_len, count = len(grid), len(grid[0]), 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '1':
                    self.bfs(grid,row,col)
                    count += 1
        return count
    
    def bfs(self, grid, row, col):
        row_len, col_len = len(grid), len(grid[0])
        if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != '1': return
        queue = collections.deque()
        queue.append((row,col))
        #mark visited
        grid[row][col] = '$'
        while queue:
            (row,col) = queue.pop()
            if row - 1 >= 0 and grid[row-1][col] == '1':
                queue.append((row-1,col))
                grid[row-1][col] = '0'
            if row + 1 < row_len and grid[row+1][col] == '1':
                queue.append((row+1,col))
                grid[row+1][col] = '0'
            if col - 1 >= 0 and grid[row][col-1] == '1':
                queue.append((row,col-1))
                grid[row][col-1] = '0'
            if col + 1 < col_len and grid[row][col+1] == '1':
                queue.append((row,col+1))
                grid[row][col+1] = '0'
            
        