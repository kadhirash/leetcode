class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # sort the array of nums
        # find the largest (end-1), 2nd largest (end -2)
        # check if largest >= 2 * 2nd largest
            # if true, return i 
            # else return -1
        # if length 1, return 0
            
        max_num = max(nums)
        if all(max_num >= 2*x for x in nums if x != max_num):
            return nums.index(max_num)
        return -1
                