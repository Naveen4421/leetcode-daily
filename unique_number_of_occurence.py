def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq=Counter(arr)  # count the uniqueness count of the numbers
        values=freq.values() #extract occurence count
        return len(values)==len(set(values)) #checking if all values are having unique count
        
