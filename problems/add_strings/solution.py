class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        stack = []
        
        carry = 0
        
        nums1 = list(num1)
        nums2 = list(num2)
        
        while len(nums1) > 0 or len(nums2) > 0  or carry:
            if len(nums1) > 0:
                x1 = ord(nums1.pop())- ord('0')
            else:
                x1 = 0
            if nums2:
                x2 = ord(nums2.pop())- ord('0')
            else:
                x2 = 0
                
            temp = x1+ x2 + carry
            stack.append(temp % 10)
            carry = temp // 10
            
        
        ans = ''
        for nums in stack:
            ans += ''.join(str(nums))
        return ans[::-1]
        
            
                