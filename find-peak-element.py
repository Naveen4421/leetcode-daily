def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        max_value=nums[0]
        for i in range(n):
            if nums[i]>=max_value:
                max_value=nums[i]
                index=i
        return index
