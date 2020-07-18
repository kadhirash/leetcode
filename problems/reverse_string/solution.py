class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2 pointers 
        # 1 pointer starts at the front of the string
        # 1 pointer starts at the back of the string 
        # increment the front, decrement the back
        
        front = 0
        back = len(s)-1 
        
        while front < back:
            s[front],s[back] = s[back], s[front]
            back -= 1
            front += 1