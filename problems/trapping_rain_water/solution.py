class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # find index max height
        max_h = height.index(max(height))
        
        # assume height[-1] is max height
        def trapping_water_till_end(height):
            partial_sum, highest_level_seen = 0, float('-inf')
            
            for h in height:
                if h >= highest_level_seen:
                    highest_level_seen = h
                else:
                    partial_sum += highest_level_seen - h
            return partial_sum
        
        return trapping_water_till_end(height[:max_h]) +\
                trapping_water_till_end(reversed(height[max_h + 1:]))
                    
        