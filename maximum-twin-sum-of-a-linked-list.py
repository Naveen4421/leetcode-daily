def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        n = len(vals)
        max_sum = 0
        for i in range(n // 2):
            twin_sum = vals[i] + vals[n - 1 - i]
            if twin_sum > max_sum:
                max_sum = twin_sum
        
        return max_sum
