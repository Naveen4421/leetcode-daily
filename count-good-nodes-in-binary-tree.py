def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Count this node if it's “good”
            count = 0
            if node.val >= max_so_far:
                count = 1
                max_so_far = node.val
            
            # Recurse for children with updated max_so_far
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            return count
        
        # Start with a very small number so root is counted if possible
        return dfs(root, float('-inf'))
