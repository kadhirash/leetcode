'''   
    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
        Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed. -> returns 0

    If no valid conversion could be performed, a zero value is returned.
    '''
class Solution:
    def myAtoi(self, str: str) -> int:
        number, negative = 0, 1
        
        str = str.strip() 
        
        MIN, MAX = -2**31, 2**31-1
        
        for i, ch in enumerate(str):
            if ch.isnumeric():
                number = number*10 + int(ch)
                if number * negative >= MAX:
                        return MAX
                if number * negative <= MIN:
                        return MIN
            elif i == 0 and ch == '+':
                pass
            elif i == 0 and ch == '-':
                negative = -1
            else:
                break
        return number * negative
        
            