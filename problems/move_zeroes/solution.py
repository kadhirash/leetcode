class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0 
        for i in range(len(arr)):
            if arr[i] != 0:
                if i != zero:
                    arr[i], arr[zero] = arr[zero], arr[i]
                zero += 1