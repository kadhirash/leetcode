class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # return the sum  of num times of char s in J for s in S
        #return sum(s in J for s in S) 
        return sum(s in set(J) for s in S)