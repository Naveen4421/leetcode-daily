def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()  # Lexicographically sort
        ans = []
        
        prefix = ""
        start = 0
        
        for ch in searchWord:
            prefix += ch
            # Find leftmost index where product >= prefix
            start = bisect.bisect_left(products, prefix, start)
            
            # Collect up to 3 matching suggestions
            suggestions = []
            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            
            ans.append(suggestions)
        
        return ans
