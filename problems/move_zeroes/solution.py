class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for i, value in enumerate(nums):
            if nums[i] != 0:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor += 1