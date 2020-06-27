class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, x in enumerate(nums):
            if x in hashm:
                return [hashm[x],i]
            else:
                hashm[target-x] = i
                
                
                
        
        
        