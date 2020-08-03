class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target and i!=j:
        #             return [i,j]
        
        # ans = { }
        # for i, val in enumerate(nums):
        #     remains = target - val
        #     if remains in ans:
        #         return [ans[remains], i]
        #     ans[val] = i
        
        ans = {}
        for i in range(len(nums)):
            remain = target-nums[i]
            if remain not in ans:
                ans[nums[i]] = i
            else:
                return [ans[remain], i]
        