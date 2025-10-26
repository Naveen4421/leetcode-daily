def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                # check if row i == column j
                equal = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        equal = False
                        break
                if equal:
                    ans += 1
        return ans
