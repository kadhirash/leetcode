class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index,values in enumerate(nums):
            complement = target - nums[index]
            if complement in indices:
                return [indices[complement], index]
            indices[values] = index
        return indices
                