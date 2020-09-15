class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        if not nums:
            return all_subsets
        for num in nums:
            for idx in range(len(all_subsets)):
                all_subsets.append(all_subsets[idx]+[num])
        return all_subsets