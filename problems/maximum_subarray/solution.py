class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # start from nums[1...n], n = length of array
        
        for i in range(1,len(nums)):
            
            if nums[i-1] > 0: # prev value > 0, then add 
                
                nums[i] += nums[i-1]
        return max(nums)