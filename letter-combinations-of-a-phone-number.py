def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping telephone digits to letters
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans = []

        def dfs(index, path):
            # If complete combination formed
            if index == len(digits):
                ans.append(path)
                return

            # Get letters corresponding to current digit
            letters = mp[digits[index]]
            for ch in letters:
                dfs(index + 1, path + ch)

        dfs(0, "")
        return ans
