import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # strat:
            # use a DFS 
            
            # iterate through ticks
                # create an adj .list between the airports
            # sort them lexicographically
        
            
        adj_list = collections.defaultdict(deque)
        # created the adj. list
        for i, j in sorted(tickets): 
            adj_list[i].append(j) # from --> to
    
        
         # dfs
        ans, stack = deque([]), ['JFK']
        while stack:
            while adj_list[stack[-1]]:
                stack.append(adj_list[stack[-1]].popleft())# pop from front until dead end
            ans.appendleft(stack.pop())
        return ans
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ans = []
        adj_list = defaultdict(list)
        for i,j in tickets:
            adj_list[i].append(j)
        
        
        for keys in adj_list:
            adj_list[keys] = sorted(adj_list[keys])
        
        def dfs(airport):
            while adj_list[airport]:
                person = adj_list[airport].pop(0)
                dfs(person)
            ans.append(airport)
            
        dfs("JFK")
        
        return reversed(ans)
        