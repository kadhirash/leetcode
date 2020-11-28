class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0: return 0
        steps = 0
        
        x, y = abs(x), abs(y)
        while x > 4 or y > 4:
            if x > y:
                x -= 2
                y -= 1 if y > 0 else -1
            else:
                y -= 2
                x -= 1 if x > 0 else -1
            steps += 1
        
        
        queue, seen = deque([(0, 0)]), {(0, 0)}
        while queue:
            steps += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r+1, c+2), (r+1, c-2), (r-1, c+2), (r-1, c-2),
                               (r+2, c+1), (r+2, c-1), (r-2, c+1), (r-2, c-1)):
                    if (nr, nc) == (x, y):
                        return steps
                    if (nr, nc) not in seen:
                        queue.append((nr, nc)); seen.add((nr, nc))