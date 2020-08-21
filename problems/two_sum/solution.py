class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return i,j
        # ans = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in ans:
        #         return (ans[complement], i)
        #     else:
        #         ans[nums[i]] = i
        
        ans = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in ans:
                return ans[complement],i
            else:
                ans[val] = i