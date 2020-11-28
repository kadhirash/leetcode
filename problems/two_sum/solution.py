class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,v in enumerate(nums):
            comp = target-v
            if comp in hm:
                return [hm[comp],i]
            else:
                hm[v] = i