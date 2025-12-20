def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Initialize queue & count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If no fresh oranges, answer = 0
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # BFS
        while q and fresh > 0:
            # process all oranges at this minute
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # check boundaries & fresh orange
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        # If there are still fresh oranges, return -1
        return minutes if fresh == 0 else -1
