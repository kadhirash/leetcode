class Solution:
    def isPalindrome(self, x: int) -> bool:
        # strat:
            # reverse half the numbers -> O(logn)
                # compare 1/2 with other 1/2
                # pop modulo operator 10 -> pop off the last digit
                # multiply the number * 10 
                    # sum of mult + pop
                # divide num // 10
            # if negative, not 0, and ends with 0: return False
        # ex:
            # 12321 
        
        
        
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        
        revert_num = 0
        
        while x > revert_num:
            pop = x % 10
            revert_num = revert_num * 10 + pop
            x = x // 10
            
        
        return x == revert_num or x == revert_num//10
            