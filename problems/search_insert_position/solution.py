class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            ans = (left + right) // 2
            if nums[ans] == target:
                return ans
            if target < nums[ans]:
                right = ans - 1
            else:
                left = ans + 1
        return left