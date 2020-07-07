class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # 4, 9 , 9
        # 5 0 0 
        # [9,9]
        # [1,0,0]
        for i in range(len(digits)):
            replace = len(digits) -i - 1
            if digits[replace] == 9:
                digits[replace] = 0
            else:
                digits[replace] += 1
                
                return digits
        
        return [1] + digits