def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        counts = Counter(arr)
        freqs = counts.values()
        return len(freqs) == len(set(freqs))
