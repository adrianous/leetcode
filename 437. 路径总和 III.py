# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(node: TreeNode, curr):
            ret = 0
            curr += node.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            prefix[curr] -= 1
            return ret

        return dfs(root, 0)

    def pathSum1(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        def get_parent_num(node):
            nums = node.nums
            if node.left:
                node.left.nums = list(map(lambda a: a + node.left.val, nums))
                node.left.nums.append(node.left.val)
                get_parent_num(node.left)

            if node.right:
                node.right.nums = list(map(lambda a: a + node.right.val, nums))
                node.right.nums.append(node.right.val)
                get_parent_num(node.right)

        root.nums = [root.val, ]
        get_parent_num(root)
        line_num = [0]

        # 后续遍历
        def get_line(node):
            if not node:
                return
            get_line(node.left)
            get_line(node.right)
            line_num[0] += node.nums.count(targetSum)

        get_line(root)
        return line_num[0]


if __name__ == '__main__':
    print(Solution().pathSum(None, 1))
