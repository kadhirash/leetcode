class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return None
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        for i in ans:
            if ans[i] == 1:
                return i
        return None
    
    
    
   