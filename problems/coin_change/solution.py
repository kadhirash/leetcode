class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # goal: min. # of coins to make up that amount
            # dp[amount]
        # state: 
            # dp[i]:  min. # of coins to make up i
        
        # base case:
            # dp init to inf.
            # dp[0] = min num of coins to make 0
        
        # recurrence:
            # for coin in coins:
                # dp[i] = min(dp[i], dp[i-coin]+1)
        # order of iteration:
            # for i in range(amount + 1):
                # for coin in coins:
                    # dp[i] = min(dp[i], dp[i-coin]+1)
        
        dp = [float('inf') for _ in range(amount+1)]
        
        dp[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+ 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
