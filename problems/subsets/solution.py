class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # strat:
            # use a stack to hold the empty set -> []
            # append the subsets to the stack if exits in nums
        
        
        ans =[ []  ]
        
        for ints in nums:
            for curr_int in ans:
                ans = ans + [curr_int + [ints]]
        return ans