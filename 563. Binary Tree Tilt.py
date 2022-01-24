# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, ret_left = dfs(node.left)
            right_sum, ret_right = dfs(node.right)
            return left_sum + right_sum + node.val, abs(left_sum - right_sum) + ret_left + ret_right

        return dfs(root)[1]
