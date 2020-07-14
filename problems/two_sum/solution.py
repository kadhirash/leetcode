class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
    ##TLE
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target and i!= j:
#                     return i,j
        
        
        
        hash_map = {}
        for i, x in enumerate(nums):
           
            if x in hash_map:
                return [hash_map[x],i]
            else:
                hash_map[target - x] = i
              
        