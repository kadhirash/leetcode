class Solution:
    # if right_max > left_max, water depends on left_max
    # if left_max > right_max, water depends on right_max
    
            # dependant on the min of both maxes 
            # max on right side --> left 
            # max on left side -> right
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1             # 0 ... 12
        
        max_left = max_right = 0
        
        ans = 0
        
        
        while left < right: # check when left < right                       # 0 < 12
            if height[left] < height[right]: # elev. on right >             # since right side >, check left
                
                if max_left <= height[left]: # value at elev > max_left      # 
                    max_left = height[left]
                else:
                    ans += max_left - height[left]                          #
                left += 1
            else: # elev on left > 
                
                if max_right <= height[right]:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans