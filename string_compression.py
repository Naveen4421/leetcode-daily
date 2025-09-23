def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        res = 0  # write pointer
        i = 0    # read pointer
    
        while i < n:
            char = chars[i]
            count = 0
        
            # count occurrences of current char
            while i < n and chars[i] == char:
                i += 1
                count += 1
        
            # write the char
            chars[res] = char
            res += 1
        
            # write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[res] = c
                    res += 1
   
        return res
