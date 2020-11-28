class Solution:
    def isPalindrome(self, x: int) -> bool:
        # revert half the numbers
        # 0 is a palindrome
            # 1-9 not a palindrome
            # can't end with 0
            
        
        
        if x < 0 or (x !=0 and x % 10 == 0):
            return False
        
        revert_num = 0
        while x > revert_num:
            pop = x % 10 
            revert_num = revert_num * 10 + pop
            x = x // 10
            
        
        return revert_num == x or revert_num // 10 == x
            
        