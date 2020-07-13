class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Plan 
        # for loop through the array 
        # if 9 at the end --> 0 
        # increment by one 
        # return new array
        
        
        for i in range(len(digits)):
            n = len(digits)-1-i # second to last digit
            
            if digits[n] == 9:
                digits[n] = 0
            else:
                digits[n] += 1
                return digits
        
        return [1] + digits