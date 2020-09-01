class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #pivot = nums[i]
        #left sum = nums[i-1], since nums[i] is the pivot 
        #right_sum = total_sum - left_sum - nums[i]
        total_sum, left_sum = sum(nums), 0
        for i in range(len(nums)):
            pivot = nums[i]
            if i != 0:     
                left_sum += nums[i-1]
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1