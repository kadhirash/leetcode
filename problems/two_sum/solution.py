class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in ans:
                return ans[comp],i
            else:
                ans[nums[i]] = i
                