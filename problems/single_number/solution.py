class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # find the number that doesn't appear twice
        
        ans = 0
        for i in nums:
            ans ^= i
        return ans