class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # strat:
            # add up all the costs from city_a
            # take the differences from second city - first city
            # sort by the least negative values
                # -350, -10 ...
            # have a separate "refund" array to add to the costs
                # ensure you have even amount from both cities as well as min. cost
                
        
        
        city_one = []
        differences = []
        n = len(costs) // 2
        min_cost = 0
        for a,b in costs:
            city_one.append(a)
            differences.append(b-a)
        min_cost = sum(city_one)
        differences.sort()
        
        for refund in range(n):
            min_cost += differences[refund]
            
        return min_cost