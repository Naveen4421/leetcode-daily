def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        i,j=0,len(s)-1
        vowels_list=[]
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        while i<=j:
            if s[i] not in vowels:
                i+=1
                continue
            if s[j] not in vowels:
                j-=1
                continue
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return''.join(s)
