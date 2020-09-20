class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        tot_water = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                tot_water += l_max - height[left]
                left += 1
            else:
                tot_water += r_max - height[right]
                right -= 1
        return tot_water