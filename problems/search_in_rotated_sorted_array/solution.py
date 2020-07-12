class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 4 5 6 7 0 1 2 --> 0
        # mid = 4 + (7-4) // 2 -> 3.5 ---> 3
        
        # 
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
            else:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else: 
                    right = mid - 1
        return -1

   