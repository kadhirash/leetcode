class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = [ [] ]
        
        
        ans = [ [] ]
        
        for ints in nums:
            for curr_int in ans:
                ans = ans + [curr_int + [ints]]
        return ans
                    