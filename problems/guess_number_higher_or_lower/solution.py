# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n
        
        while left <= right:
            middle = left + (right - left) // 2
            ans = guess(middle)
            if ans == -1:
                right = middle - 1
            elif ans == 1:
                left = middle + 1
            else:
                return middle
                
        return -1
                