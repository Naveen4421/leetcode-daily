class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # Each day’s span starts at 1 (today itself)
        span = 1
        
        # Pop all prices that are <= current price
        # and add their spans to current span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price with its span
        self.stack.append((price, span))
        
        return span
