class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's alg (DP)
        # # check i from 1 --> length of nums
        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0: # if last element > 0, add to nums
        #         nums[i] += nums[i-1]
        # return max(nums)        
        
        
        m = nums[0]
        tempm = nums[0]
        for i in nums[1:]:
            if i > tempm and tempm < 0:
                tempm = i
            else:
                tempm += i
            
            if tempm > m:
                m = tempm
            
                
        return m