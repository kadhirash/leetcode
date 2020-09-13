class Solution:
    def removeDuplicates(self, S: str) -> str:
        # remove the 2 adjacent and equal letters until no more duplicates
        
        # Clarification:
            # S = lowercase letters
        
        # Example:
            # abbaca
                # aaca
                # ca
        # WalkThrough:
            # create a stack to hold answer -> O(n-d) space
            # in stack, add string chars
                # if the last string char on stack == next string char, then pop 
            # repeating until no more can be removed
            # return as a string form
            
        
        i,n = 0,len(S)
        res = list(S)
        for j in range(n):
            res[i]=res[j]
            if i>0 and res[i-1]==res[j]:
                i-=2
            i+=1
        return ''.join(res[:i])