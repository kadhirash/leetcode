class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        snums = sorted(nums)
        for i in range(len(snums)):
            if snums[i] not in d:
                d[snums[i]]=i       
        return [ d[n] for n in nums ]