class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(i,nums[i]) for i in range(len(nums))], key=lambda y : y[1])
        
        j = 0
        i=0
        while i < len(nums):
            while j < i and nums[i][1] - nums[j][1] > t:
                j+=1
            for l in range(j,i):
                if abs(nums[l][0] - nums[i][0]) <= k:
                    return True
            i+=1        
            
        return False