class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[right]: # left sorted 
                if nums[left] <= target and target <= nums[mid]: #answer on left side
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right sorted
                if nums[mid] <= target and target <= nums[right]: # answer on right side
                    left = mid + 1
                else:
                    right = mid - 1
        return -1