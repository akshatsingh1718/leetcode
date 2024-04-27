from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        range_sum = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal low, high, range_sum

            if root is None:
                return

            dfs(root.left)
            dfs(root.right)

            range_sum += root.val if (low <= root.val <= high) else 0

        dfs(root)
        return range_sum


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low = 7
high = 15
output= 32

print(Solution().rangeSumBST(root, low, high))
