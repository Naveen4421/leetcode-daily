def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=[]
        for i in s:
            if i=="*":
                n.pop()
            else:
                n.append(i)
        return ''.join(n)
