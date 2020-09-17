class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #to do:
            # return all possible subsets 
        # ex:
            # [1,2,3]
            # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        # strat:
            # have an ans arr. holding []
                # iterate through the digits in num
                    # append the possible subsets(curr_int + digits) to the arr
            # return arr
            
            
        ans = [ [] ]
        
        for digs in nums:
            for curr_dig in ans:
                ans = ans + [curr_dig + [digs]]
        return ans
            