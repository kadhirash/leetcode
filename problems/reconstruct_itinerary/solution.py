class Solution:
    def dfs(self,airport):
        while self.adj_list[airport]:
            person = self.adj_list[airport].pop(0)
            self.dfs(person)
        self.ans.append(airport)
    
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.ans = []
        self.adj_list = defaultdict(list)
        
        for i,j in tickets:
            self.adj_list[i].append(j) # from --> to
            
        # sort lexico. by the keys in adj. list
        for keys in self.adj_list:
            self.adj_list[keys].sort()
            
        
        self.dfs("JFK")
        
        return reversed(self.ans)