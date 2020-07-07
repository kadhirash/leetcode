class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashl = {}
        
        for i, iterate in enumerate(nums):
            if iterate in hashl:
                return [hashl[iterate], i]
            else:
                hashl[target-iterate] = i