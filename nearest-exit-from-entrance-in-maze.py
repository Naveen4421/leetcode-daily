def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque
        rows, cols = len(maze), len(maze[0])
        sr, sc = entrance
        visited = set([(sr, sc)])
        
        # BFS queue: (row, col, distance_from_entrance)
        q = deque([(sr, sc, 0)])
        
        while q:
            r, c, dist = q.popleft()
            
            # Check all 4 directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                
                # Skip invalid or wall
                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    maze[nr][nc] == '+' or
                    (nr, nc) in visited):
                    continue
                
                # Mark visited
                visited.add((nr, nc))
                
                # Check if exit:
                # Must be on boundary and NOT the entrance
                if (nr == 0 or nr == rows-1 or
                    nc == 0 or nc == cols-1):
                    
                    # Not the entrance
                    if [nr, nc] != entrance:
                        return dist + 1
                
                # Add to queue
                q.append((nr, nc, dist + 1))
        
        # No reachable exit
        return -1
