def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort by end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        curr_end = points[0][1]
        
        for start, end in points:
            # If this balloon starts after the current end point,
            # we need a new arrow
            if start > curr_end:
                arrows += 1
                curr_end = end
        
        return arrows
