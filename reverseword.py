def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #s=set(s)
        s=s.split()
        s=list(s)
        result=s[::-1]
        return ' '.join(result)
