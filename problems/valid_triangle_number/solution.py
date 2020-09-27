class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # a+ b > c
        # b + c > a 
        # a + c > b
        
        if not nums:
            return 0
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n-1,1,-1):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += right - left
                    right -= 1
        return ans