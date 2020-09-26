class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        
        max_left = max_right = 0
        
        ans = 0
        
        
        while left < right:
            
            if height[left] < height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
                
            else: # height[right] >= height[left]
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans
                
                
    
