class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # strat:
            # use a DFS 
            
            # iterate through ticks
                # create an adj .list between the airports
            # sort them lexicographically
        
            
        ans = []
        adj_list = defaultdict(list)
        # created the adj. list
        for i, j in tickets:
            adj_list[i].append(j) # from --> to
            
        
        # sort lexicographically
        for keys in adj_list:
            adj_list[keys] = sorted(adj_list[keys]) # Onlogn
        
        
        # dfs
        
        def dfs(airport):
            while adj_list[airport]:
                candidate = adj_list[airport].pop(0)
                dfs(candidate)
            ans.append(airport)
        dfs('JFK')
        
        return reversed(ans)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        