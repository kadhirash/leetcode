class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
            if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
                continue 
            mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1 
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.add(tuple(sorted([nums[left], nums[mid], nums[right]])))
                    # while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                    #     mid += 1
                    # while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                    #     right -= 1
                    mid += 1
                    right -= 1
        return result
    
    
    
    
#     res = set()
#     nums.sort()
#     n = len(nums)
#     for i in range(n-2):
#         if i > 0 and nums[i-1] == nums[i]:
#             continue
#         l, r = i+1, n-1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s < 0:
#                 l += 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
#                 l += 1
#                 r -= 1
#     return [list(i) for i in res]