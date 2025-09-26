def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            h=min(height[l],height[r])
            width=r-l
            area=width*h
            if max_area<area:
                max_area=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
