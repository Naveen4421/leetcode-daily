def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        pairs = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        
        # Sort descending by nums2
        pairs.sort(reverse=True, key=lambda x: x[0])

        min_heap = []
        sum_nums1 = 0
        max_score = 0

        for val2, val1 in pairs:
            # Add val1 to heap
            heapq.heappush(min_heap, val1)
            sum_nums1 += val1

            # If we have more than k in the heap, drop the smallest
            if len(min_heap) > k:
                popped = heapq.heappop(min_heap)
                sum_nums1 -= popped

            # If we have exactly k, update max score
            if len(min_heap) == k:
                max_score = max(max_score, sum_nums1 * val2)

        return max_score
