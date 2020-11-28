class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, size = [ [] ], 0 
        nums.sort()
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                k = size
            else:
                k = 0
            size = len(ans)
            for j in range(k,size):
                
                ans = ans + [ans[j] + [nums[i]]]
        return ans