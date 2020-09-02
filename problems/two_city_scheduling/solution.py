class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first_city= []
        for city_one,city_two in costs:
            first_city.append(city_one)
        diff = []
        for city_one, city_two in costs:
            diff.append(city_two-city_one)
            
        refund = diff.sort()
        refund = diff[:len(costs)//2]
        
        return sum (first_city + refund)