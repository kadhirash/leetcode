class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # N = people
        # a trusts b
        # any person is trusted by N - 1 person and the same person believes no one, then they are a judge

        trusts = [0] * (N+1)
        #print(trusts) # [[0,0,0]]
        for (a, b) in trust:
            trusts[a] -= 1
            #print(f'trusts[a]: {trusts[a]}') #-1
            trusts[b] += 1
            #print(f'trusts[b]: {trusts[b]}') # 1
            
        for i in range(1,len(trusts)):
            if trusts[i] == N-1:
                #print(f'trusts[i]: {trusts[i]}')
                #print(f'N-1: {N-1}')
                #print(f'i: {i}')
                return i
        return -1