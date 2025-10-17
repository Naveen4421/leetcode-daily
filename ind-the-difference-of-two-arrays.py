def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        numset1,numset2=set(nums1),set(nums2)
        res1,res2=set(),set()
        for n in nums1:
            if n not in numset2:
                res1.add(n)
        for m in nums2:
            if m not in numset1:
                res2.add(m)
        return [list(res1),list(res2)]
