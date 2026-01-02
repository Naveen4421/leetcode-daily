def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2 = prev1
            prev1 = curr
        
        return prev1
