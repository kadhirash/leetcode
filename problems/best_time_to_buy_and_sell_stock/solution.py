class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # q&a:
            # Have to buy before you sell
            # only one transaction
        # todo:
            # find max profit
                # profit = sell - buy
        # ex:
            # [7,1,5,3,6,4]
            # 5
            
        if not prices:
            return 0
        dp = [0] * len(prices)
        min_price = prices[0]

        for i in range(len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return dp[-1]
        
        
        
            