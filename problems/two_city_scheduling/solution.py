class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 10 + 30 + 400 + 30 -> total
        # differences = b-a 
            # sort
        # n times 
        # total + n differences
        # min_cost
        
        
        min_cost = 0
        differences = []
        
        N = len(costs) // 2
        
        for a,b in costs:
            min_cost += a
            differences.append(b-a)
            
        differences.sort() # nlogn
        
        for i in range(N):
            min_cost += differences[i]
        
        return min_cost
        