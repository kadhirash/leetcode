class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not s or not nums: return 0
        min_len = float('inf')
        windowStart, windowSum = 0,0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= s:
                min_len = min(min_len, windowEnd-windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1
        if min_len == float('inf'): return 0
        return min_len