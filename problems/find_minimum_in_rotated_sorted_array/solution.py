class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search --> O(logn)
        
        # ex:
            # [3,4,5,1,2] 
            # [1,2,3,4,5]
        if not nums:
            return None
        
        left,right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]