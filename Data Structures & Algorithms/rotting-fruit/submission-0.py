class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_cnt = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_cnt += 1
                
        min_passed = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh_cnt > 0:
            for _ in range(len(q)):
                r, c = q.popleft()      
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            q.append((nr, nc))  
                            fresh_cnt -= 1

            min_passed += 1
        
        print(fresh_cnt, min_passed)
        if fresh_cnt == 0:
            return min_passed
        return -1


