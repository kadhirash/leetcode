class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        city_a, diff = [], []
        for i, j in costs:
            city_a.append(i)
        for i, j in costs:
            diff.append(j-i)
        refund = diff.sort()
        refund = diff[:len(costs) // 2]
        return sum(city_a + refund)

        