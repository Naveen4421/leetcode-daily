def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        EB=prices[0] #effective buy
        profit=0   # current profit
        for i in range(1,n):
            profit=max(profit,prices[i]-EB-fee)  # calculating currect profit by substract from privious
            EB=min(EB,prices[i]-profit)
        return profit
