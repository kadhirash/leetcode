class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through list of prices
        # find where it's the lowest and mark it as BUY
        # find after that point where it's the largest and mark that as SELL
        # SELL-BUY = PROFIT 
        
        
        #TLE due to last case 
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         min_price = prices[j] - prices[i]
        #         if(min_price > max_profit):
        #             max_profit = min_price
        # return max_profit
        
        
        min_price = float('inf')
        max_profit = 0
        
        for i in prices:
            min_price = min(min_price, i)
            #print(min_price)
            curr_profit = i - min_price
            #print(curr_profit) # 1, 2, 3, 4, 5
            max_profit = max(max_profit, curr_profit)
            #print(max_profit)
        return max_profit