class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in ans:
                return [ans[complement], i]
            else:
                ans[nums[i]] = i
        