class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        min_cost = 0
        differences = []
        n = len(costs) // 2
        for a,b in costs:
            min_cost += a
            differences.append(b-a)
            
        differences.sort()
        
        
        for refund in range(n):
            min_cost += differences[refund]
            
        return min_cost
    
        