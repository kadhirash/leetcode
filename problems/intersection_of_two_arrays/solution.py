class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_one = set(nums1)
        set_two = set(nums2)
        return set_one & set_two