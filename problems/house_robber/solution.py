class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        n(0) = nums[0]
        n(1) = max(num[0], num[1])
        n(k) = max(n(k-2) + nums[k], n(k-1))
        '''
        if not nums: 
            return 0
        if len(nums) == 1: 
            return nums[0]
        
        robber = [0] * len(nums)
        robber[0] = nums[0]
        robber[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            robber[i] = max(nums[i] + robber[i-2], robber[i-1])
        return robber[-1] 