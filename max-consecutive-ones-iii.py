def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # if current element is 0, we use one flip
            if nums[right] == 0:
                k -= 1

            #  if flips go negative, shrink from left
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            # update max length
            max_len = max(max_len, right - left + 1)

        return max_len
