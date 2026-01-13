def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # Step 1 — sort by end time
        intervals.sort(key=lambda x: x[1])

        # Step 2 — iterate keeping non-overlapping ones
        keep = 1
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                keep += 1
                end = intervals[i][1]

        # Step 3 — removals = total - kept
        return len(intervals) - keep
