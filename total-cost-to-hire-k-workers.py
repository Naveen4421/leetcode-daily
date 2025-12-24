def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        import heapq
        n = len(costs)
        
        leftHeap = []
        rightHeap = []
        
        # pointers for next eligible workers
        leftIdx = 0
        rightIdx = n - 1

        # populate heaps from both ends
        for _ in range(candidates):
            if leftIdx <= rightIdx:
                heapq.heappush(leftHeap, costs[leftIdx])
                leftIdx += 1
            if leftIdx <= rightIdx:
                heapq.heappush(rightHeap, costs[rightIdx])
                rightIdx -= 1

        total_cost = 0

        for _ in range(k):
            # pick from the cheaper top
            left_val = leftHeap[0] if leftHeap else float('inf')
            right_val = rightHeap[0] if rightHeap else float('inf')

            if left_val <= right_val:
                total_cost += heapq.heappop(leftHeap)
                # refuel from next left candidate
                if leftIdx <= rightIdx:
                    heapq.heappush(leftHeap, costs[leftIdx])
                    leftIdx += 1
            else:
                total_cost += heapq.heappop(rightHeap)
                # refuel from next right candidate
                if leftIdx <= rightIdx:
                    heapq.heappush(rightHeap, costs[rightIdx])
                    rightIdx -= 1

        return total_cost
