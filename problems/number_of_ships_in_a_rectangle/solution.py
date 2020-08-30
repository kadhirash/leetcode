# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # stop condition
        if topRight.x<bottomLeft.x or topRight.y<bottomLeft.y or not sea.hasShips(topRight, bottomLeft):
            return 0
    
        # point found
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        # divide matrix into 4 submatrix. Recursively search
        mid_x, mid_y = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
        
        cnt = 0
        cnt += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
        cnt += self.countShips(sea, topRight, Point(mid_x+1, mid_y+1)) 
        cnt += self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y+1)) 
        cnt += self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x+1, bottomLeft.y))
        
        return cnt