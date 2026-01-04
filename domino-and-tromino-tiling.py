def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        if n == 0: 
            return 1
        if n == 1: 
            return 1
        
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        
        f[0], f[1] = 1, 1
        g[0], g[1] = 0, 0
        
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + 2 * g[i - 1]) % MOD
            g[i] = (g[i - 1] + f[i - 2]) % MOD
        
        return f[n] % MOD
