from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')  # FIXED
        answer_level = 1
        level = 0

        while queue:
            level += 1
            size = len(queue)
            level_sum = 0

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level

        return answer_level
