def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, current, remaining):
            # If remaining sum is 0 and we have k numbers
            if len(current) == k and remaining == 0:
                result.append(current[:])
                return
            
            # If too many numbers or sum is too low, prune
            if len(current) > k or remaining < 0:
                return

            for num in range(start, 10):
                current.append(num)
                backtrack(num + 1, current, remaining - num)
                current.pop()
        
        backtrack(1, [], n)
        return result
