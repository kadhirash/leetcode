class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # TC: O(n^2), SC:O(1)
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             count += 1
        # return count
        
        count=0
        hashmap={}
        for index, values in enumerate(nums):
            if values in hashmap:
                count += hashmap[values]
                hashmap[values] += 1
            else:
                hashmap[values]=1
        
        return count