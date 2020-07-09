class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # no need to check for non-empty
        
        #increase one to integer
        # sig. digit is at head of list, and no leading 0 except 0 itself
        
        # return arry with incrementation
        
        
        # Plan
        
        # Loop through array
        # if 9 at the end, change to a 0 else change last digit to + 1
        # 
        for i in range(len(digits)):
            index = len(digits)-1-i
            #print(index)
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                print(digits)
                return digits
        return [1] + digits