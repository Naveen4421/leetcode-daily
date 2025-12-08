def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        directed = set()  # store directed edges as tuple (u, v)
        
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            directed.add((u, v))
        
        self.result = 0
        visited = [False] * n
        
        def dfs(city):
            visited[city] = True
            for nei in adj[city]:
                if not visited[nei]:
                    # if original edge was city->nei, we need to reverse it
                    if (city, nei) in directed:
                        self.result += 1
                    dfs(nei)
        
        dfs(0)
        return self.result
