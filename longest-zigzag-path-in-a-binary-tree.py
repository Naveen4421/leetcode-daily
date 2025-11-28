def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        
        def dfs(node, from_left, left_len, right_len):
            if not node:
                return
            # Update global answer
            self.ans = max(self.ans, left_len, right_len)
            # Go left: last move becomes left, so extend right → left switch
            dfs(node.left, True, 0, left_len + 1)
            # Go right: last move becomes right, so extend left → right switch
            dfs(node.right, False, right_len + 1, 0)
        
        # Starting at root: no prior move, treat as coming from neither side
        dfs(root, False, 0, 0)
        return self.ans
