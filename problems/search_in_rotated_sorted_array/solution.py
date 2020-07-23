class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0 log(n) = binary search
        # 3 cases 
        # 1) if mid == target, return mid
        # 2) if mid > right, left is sorted 
            # left <= target <= mid
        # 3)  right side is sorted
            # mid <= target <= right
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            # case 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]: # left sorted
                if nums[left] <= target and target <= nums[mid]: #answer on left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]: #answe on right
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 # return -1 if nothing found 
