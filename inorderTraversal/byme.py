from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime
    Details
    38ms
    Beats 73.01%of users with Python3
    Memory
    Details
    16.26MB
    Beats 71.72%of users with Python3
    """

    def traversal(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if root is None:
            return

        if root.left is not None:
            self.traversal(root.left, arr)

        arr.append(root.val)

        if root.right is not None:
            self.traversal(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.traversal(root, arr)

        return arr


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    s = Solution()

    print(s.inorderTraversal(root))
