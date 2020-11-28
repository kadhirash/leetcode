class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count variable for number of continuous subarrays, sum = k
        count, sum_val = 0,0
        ans = {0:1}
        for i in range (len(nums)):
            sum_val += nums[i]
            if sum_val - k in ans:
                count += ans[sum_val - k]
            if sum_val not in ans:
                ans[sum_val] = 1
            else:
                ans[sum_val] += 1
        return count
    
    
    

    