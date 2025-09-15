def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer=[]
        i , j =0,0
        while i<len(word1) and j<len(word2):
            answer.append(word1[i])
            answer.append(word2[j])
            i+=1
            j+=1
        answer.append(word1[i:])
        answer.append(word2[j:])
        return"".join(answer)
