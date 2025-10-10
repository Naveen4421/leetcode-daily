def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        count=0
        max_average=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        max_count=count

        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            max_count=max(max_count,count)
        return max_count
