class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans, count = {}, 0
        for i in range(len(nums)):
            if nums[i] in ans:
                count += 1
                return True
            else:
                ans[nums[i]] = i
        return False