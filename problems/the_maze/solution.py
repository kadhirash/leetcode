class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ylen, xlen = len(maze), len(maze[0])
        L, R, T, B = 'LRTB'

        y, x = start
        q = deque([(None, y, x)])
        maze[y][x] = 9

        while q:
            prev, y, x = q.popleft()

            my = maze[y]

            if prev != R:
                x1 = x
                while x1 + 1 < xlen and my[x1 + 1] != 1:
                    x1 += 1
                if [y, x1] == destination:
                    return True
                elif my[x1] == 0:
                    my[x1] = 9
                    q.append((L, y, x1))

            if prev != L:
                x1 = x
                while 0 <= x1 - 1 and my[x1 - 1] != 1:
                    x1 -= 1
                if [y, x1] == destination:
                    return True
                elif my[x1] == 0:
                    my[x1] = 9
                    q.append((R, y, x1))

            if prev != T:
                y1 = y
                while y1 + 1 < ylen and maze[y1 + 1][x] != 1:
                    y1 += 1
                if [y1, x] == destination:
                    return True
                elif maze[y1][x] == 0:
                    maze[y1][x] = 9
                    q.append((B, y1, x))

            if prev != B:
                y1 = y
                while 0 <= y1 - 1 and maze[y1 - 1][x] != 1:
                    y1 -= 1
                if [y1, x] == destination:
                    return True
                elif maze[y1][x] == 0:
                    maze[y1][x] = 9
                    q.append((T, y1, x))

        return False