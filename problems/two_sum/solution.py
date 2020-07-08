class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices of 2 numbers so it adds up to target
        # only 1 solution
        
        
        # for loop to iterate through the array
        # 2nd for loop to keep track of indices
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                #print(i,j)
                if nums[i] + nums[j] == target and i!= j:
                    return i,j
                    