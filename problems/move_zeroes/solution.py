class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero = 0 
        # for i in range(len(arr)):
        #     if arr[i] != 0:
        #         if i != zero:
        #             arr[i], arr[zero] = arr[zero], arr[i]
        #         zero += 1
                
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0