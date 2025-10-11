def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_average=0
        left=0
        zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>1:
                if nums[left]==0:
                    zero-=1
                left+=1
            max_average=max(max_average,right-left)
        return max_average
