def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        ans=[]
        max_value=max(candies)
        for i in candies:
            result.append(i+extraCandies)
        ans = [x >= max_value for x in result]
        return ans
