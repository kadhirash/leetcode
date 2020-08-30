class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return i,j
        
        ans = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in ans:
                return ans[complement],i
            else:
                ans[nums[i]] = i
        