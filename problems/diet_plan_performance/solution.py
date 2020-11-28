class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = max_sum = 0
        for i in range(len(calories)-k+1):
            if i == 0:
                max_sum = sum(calories[i: i + k])
            else:
                max_sum = max_sum-calories[i-1] + calories[i+k-1]
            if max_sum < lower: score -= 1
            elif max_sum > upper: score += 1
        return score