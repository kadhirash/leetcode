class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         for counter, value in enumerate(nums):
#             #print(counter,value)
#             if value == target:
#                 return counter
#             else:
                
    
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            # Check if x is present at mid 
            if nums[mid] < target: 
                low = mid + 1
  
            # If x is greater, ignore left half 
            elif nums[mid] > target: 
                high = mid - 1

            # If x is smaller, ignore right half 
            else: 
                return mid 
  
        # If we reach here, then the element was not present 
        return low
        