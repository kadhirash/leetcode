class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 2n people
        # acosti = citya, bcosti = city b
        # return min. cost to fly every person, so citya = cityb 
        
        
        # 2n == len(costs)
        
        # each city = [i,j]
        # get city[i] of city a values
        # find differences between city[j-i] 
        
            # Since some neg., sort them and then return the smallest values
        # return sum of city a + smallest diff value
        
        
        city_a = []
        for a,b in costs:
            city_a.append(a)
        diff = []
        for a,b in costs:
            diff.append(b-a)
        
        small = diff.sort()
        small = diff[:len(costs)//2]
        return sum(city_a + small)