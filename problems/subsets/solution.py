class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ints in nums:
            ans += [curr_int + [ints] for curr_int in ans]
        return ans