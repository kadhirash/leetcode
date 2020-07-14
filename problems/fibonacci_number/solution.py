class Solution:
    def fib(self, N: int) -> int:
        # recursion
        # if N <= 1:
        #     return N
        # else:
        #     return self.fib(N-1) + self.fib(N-2)
        
        # memoization
        
        cache = {}
        def mem(N):
            if N in cache:
                return cache[N]
            
            if N < 2:
                result = N
            else:
                result = mem(N-1) + mem(N-2)
                
            
            cache[N] = result
            return result
        
        return mem(N)
            