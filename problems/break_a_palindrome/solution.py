class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if not palindrome: return None
        elif len(palindrome) == 1:
            return ''
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a': 
                # everything before i, add 'a', everything after i
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
        
        