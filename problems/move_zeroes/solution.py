class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i]
        #         index += 1
        # for i in range(index, len(nums)):
        #     nums[i] = 0
        