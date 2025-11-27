def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # base: empty path has sum 0
        self.count = 0

        def dfs(node, currSum):
            if not node:
                return
            currSum += node.val
            # If there was a prefix sum = currSum - targetSum, then
            # there is a path ending here summing to targetSum.
            self.count += prefix_counts[currSum - targetSum]

            # Add current sum to map
            prefix_counts[currSum] += 1

            # Recurse
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            # Backtrack: remove current sum before returning to parent
            prefix_counts[currSum] -= 1
