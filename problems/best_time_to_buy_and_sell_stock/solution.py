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
            
        
        min_buy, max_profit = float('inf'), float('-inf')
        
        if not prices: return 0
        
        for price_of_stock in prices:
            min_buy = min(min_buy, price_of_stock)
            profit = price_of_stock - min_buy
            max_profit = max(max_profit, profit)
            
        return max_profit
        
        
        
            