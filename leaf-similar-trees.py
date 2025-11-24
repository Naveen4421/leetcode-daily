def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def collect_leaves(node, leaves):
            if not node:
                return
            # If it's a leaf:
            if node.left is None and node.right is None:
                leaves.append(node.val)
            # Recurse left then right:
            collect_leaves(node.left, leaves)
            collect_leaves(node.right, leaves)
        
        leaves1 = []
        leaves2 = []
        collect_leaves(root1, leaves1)
        collect_leaves(root2, leaves2)
        
        return leaves1 == leaves2
