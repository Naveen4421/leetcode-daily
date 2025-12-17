def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(start, end, visited):
            if start == end:
                return 1.0  # x / x = 1

            visited.add(start)
            for nei, weight in graph[start]:
                if nei in visited:
                    continue
                res = dfs(nei, end, visited)
                if res != -1:  # valid path found
                    return weight * res

            return -1.0

        answers = []
        for x, y in queries:
            if x not in graph or y not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(x, y, set()))

        return answers
