class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # start at 0,0
        # Return True if crosses ppoint
        # Return False
        
        #N: (0,1)                   x = curr_pt[0] + directions[point][0] 
        #W: (-1,0)                  y = curr_pt[1] + directions[point][1]
        #S: (0, -1)
        #E: (1,0)                       
        
        curr_pt = (0,0)
        
        seen_pt = {curr_pt}
        
        directions = {'N':(0,1), 'W': (-1,0), 'S': (0,-1), 'E': (1,0)}
        
        for point in path:
            curr_pt = curr_pt[0] + directions[point][0], curr_pt[1] + directions[point][1]
            if curr_pt in seen_pt:
                return True
            seen_pt.add(curr_pt)
        return False