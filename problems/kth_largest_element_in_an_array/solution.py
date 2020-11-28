class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 6 , 5 ,4, 3 , 2 , 1 
        
        ans = sorted(nums,reverse = True)
        #print(ans)
        return ans[k-1]