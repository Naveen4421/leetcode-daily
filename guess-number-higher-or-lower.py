def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,high=1,n
        while low<=high:
            mid=(low+high)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res>0:
                low=mid+1
            else:
                high=mid-1
