class Solution:
    def __init__(self):
        self.dictionary= {}
    
    def climbStairs(self, n: int) -> int:
        if n in self.dictionary:
            return self.dictionary[n]
        
        if n == 0 or n == 1:
            return 1
        else:
            ans = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.dictionary[n] = ans
            return ans