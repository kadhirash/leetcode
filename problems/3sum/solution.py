class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #store ans in a list
        ans = [ ] 
        # sort numbers from least to greatest
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums [i-1]:
                continue #to eliminate duplicate values
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0: #-4, -1, -1, 0, 1, 2
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: # make sure left doesn't repeat
                        left = left + 1
                    while left <=  right and nums[right] == nums[right - 1]: # make sure right doesn't repeat
                        right = right - 1 
                    #after making sure no duplicate left or right values
                    left = left + 1
                    right = right - 1
        return ans