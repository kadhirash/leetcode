class Solution:
    def isPalindrome(self, x: int) -> bool:
#     # first soln  
#     # base
#         if x < 0:
#             return False
#         if x > 0 and x < 10:
#             return True
#         pal = x
#         ans = 0
#         while pal:
#             ans = ans * 10 + pal % 10  # ans * 10 = save value of the other digits in front #+ pal % 10 = get last digit
#             pal = int(pal/10)
#         return ans == x
        
    # 2nd soln
    
        
        #return str(x) == str(x)[::-1]
    
    
    # 3rd soln
    
#         orig = x
#         back_x = 0
#         while x > 0:
#             back_x = (back_x * 10) + (x % 10)
#             x = x // 10
#         return orig == back_x

# 4th

        if x < 0:
            return False
        fast, slow = x, x
        reversed_half = 0
        while fast//10:
            reversed_half = reversed_half * 10 + slow % 10
            slow //= 10
            fast //= 100

        return reversed_half == slow if fast == 0 else reversed_half == slow//10