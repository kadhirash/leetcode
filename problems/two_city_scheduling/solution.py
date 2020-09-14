class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Clarifications:
            # len(costs) = even
            # 2n people -> n people in A, n people in B
        # Question to Solve:
            # Return min. cost to fly every person to city so n people arrive from a and b
        # Example:
            # costs = [[10,20],[30,200],[400,50],[30,20]]
            # 110
            
        # Strategy:
            # Send everyone from city A 
                # 10 30 400 30 -> 470
            # Find differences between City B and city A
                # 10 170 -350 -10
            # Sort by the differences (from least to greatest)
                # -350 -10 10 170
            # Return sum of City A values + 1/2 len of differences costs
            
        min_cost = 0
        n = len(costs) // 2
        differences = []
        for city_a,city_b in costs:
            min_cost += city_a
            differences.append(city_b-city_a)
        
        differences.sort()
        
        for refund in range(n):
            min_cost += differences[refund]
            
        return min_cost