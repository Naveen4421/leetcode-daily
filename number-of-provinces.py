def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        res = 0
        
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                res += 1
                dfs(i)
        return res
