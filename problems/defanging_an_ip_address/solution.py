class Solution:
    def defangIPaddr(self, address: str) -> str:
        # naive: O(n) 
        # ans = address.replace(".", "[.]")
        # return ans
        
       # ans = {}
    
        return ''.join('[.]' if c == '.' else c for c in address)
    
        
        
        