class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # day i = price of a stock[i]
        # can't sell stock before you buy one
        
        
        # profit: buy stock - sell price, sell price > buying price
        
        
        # min. val variable = float('inf')
        # max. profit value = 0
        
        sell_price, max_profit = float('inf'), 0
        
        
        # iterate through the prices
        
        for stock in prices:
            # update the sell_price, which is min(sell price and stock)
            sell_price = min(sell_price, stock) # 7,1,1,1,1, 1 
            profit = stock - sell_price # 7-7 = 0, 1-1 = 0 , 5-1 = 4, 3-1 = 2, 6 - 1 = 5, 4-1 = 3
            max_profit = max(max_profit, profit) # 0, 0,4, 4, 5, 5 
        return max_profit
            
        