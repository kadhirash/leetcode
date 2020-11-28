# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for i in range(n):
        #     if isBadVersion(i):
        #         return long long(i)
        # return long long(n)
        
        left, right = 1, n
        
        while left < right:                            # n = 5 
            mid = left + (right-left) // 2              # 1 2 3 4 
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left