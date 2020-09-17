class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        min_cost = 0
        differences = []
        
        for city_one, city_two in costs:
            min_cost += city_one
            differences.append(city_two-city_one)
        
        differences.sort()
        
        for refund in range(n):
            min_cost += differences[refund]
        return min_cost