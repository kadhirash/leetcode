class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)] # first col/row all 1's
        # right or down == 1 
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1] # above ,left
                
        return dp[m-1][n-1]
                
        