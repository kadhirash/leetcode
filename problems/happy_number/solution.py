class Solution:
    def isHappy(self, n: int) -> bool:
        #happy = 
        # positive integer  --- (n > 0)
        # replace num by sum of square of its digits --- replace n by sum(square of digits)
        # repeat until  == 1
        # if 1 then happy, else false 
        
        hash_set = set()
        total_sum = 0
        while n > 0 and n != 1:
            for i in str(n):
                n= sum(int(i) ** 2 for i in str(n))
            if n in hash_set:
                return False
            else:
                hash_set.add(n)
        else:
            return True
    