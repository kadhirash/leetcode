class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits 2 - 9 inclusive
        # return posisble combinations
            # answer can be in any order
        
        if not digits: return ""
        # phone in dictionary
        phone = {   '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                }
        
        ans = []
        #print(phone[digits[0]])
        
        def combine(combo, digits):
            if len(digits) == 0: # no more digits
                ans.append(combo) 
            else:
                for letters in phone[digits[0]]: # get the first digit of each segment
                    combine(combo + letters, digits[1:]) # combine the letters together and get combos, plus the digit values
        if digits:
            combine("",digits) # call recursive function
        return ans