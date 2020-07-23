class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # o(logn) again
        # 4 cases actually due to duplicate
        # 1) if nums[mid] == target, return True
        # 2) if mid > right, left is sorted 
            # left <= target <= mid
        # 3)  right side is sorted
            # mid <= target <= right 
        # if nums[mid] == nums[right]
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[right]: # left sorted
                if nums[left] <= target and target <= nums[mid]: # answer on left
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1 # redo to find new mid
            else:
                if nums[mid] <= target and target <= nums[right]: # answer on right
                    left = mid + 1
                else:
                    right = mid - 1
        return False
                