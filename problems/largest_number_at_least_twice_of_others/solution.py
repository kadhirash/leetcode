class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # find largest number using max
        max_num = max(nums)
        #iterate through nums and check if max_num is 2*nums[i]
        
        if(len(nums)) == 1:
            return nums.index(max_num)
        for i in range(len(nums)):
            max_num_i = nums.index(max_num)
        for x in range(len(nums)):
            if x != max_num_i and nums[max_num_i] < 2 * nums[x]:
                return -1
        return max_num_i
    
    
    
    #  int maxIndex = 0;
    #     for (int i = 0; i < nums.length; ++i) {
    #         if (nums[i] > nums[maxIndex])
    #             maxIndex = i;
    #     }
    #     for (int i = 0; i < nums.length; ++i) {
    #         if (maxIndex != i && nums[maxIndex] < 2 * nums[i])
    #             return -1;
    #     }
    #     return maxIndex;
    # }