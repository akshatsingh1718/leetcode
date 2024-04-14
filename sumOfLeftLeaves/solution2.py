# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def bfs(root: TreeNode, is_left: bool):
            if root is None:
                return 0

            # if leaf node found
            if root.left is None and root.right is None:
                if is_left:
                    return root.val
                else:
                    return 0

            # compute both left and right sum
            # right sum will always be zero since we are returning 0 if right leaf node
            left_sum = bfs(root.left, True)

            right_sum = bfs(root.right, False)
            return left_sum + right_sum

        return bfs(root, False)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    """
                1
        2               3
    4       5      N        6
    
    """

    s = Solution()

    print(s.sumOfLeftLeaves(root))
