class Solution:
    def findMin(self, nums: List[int]) -> int:
        # todo: find min. element
        # example:
            # [3,4,5,1,2] 
            # 1 
            
        # strat:
            # naive approach:
                # sorted --> retrn first element
        
            # use binary search
            # 
            
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]