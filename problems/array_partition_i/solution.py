class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort the array 
        nums.sort()
        sum_min = 0
        # group every 2 numbers, and find the min
        for i in range(0, len(nums),2):
            sum_min += nums[i]
        return sum_min