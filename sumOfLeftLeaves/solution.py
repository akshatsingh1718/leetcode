# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def bfs(root: TreeNode, left_sum: List[int], is_left: bool):
            if root is None:
                return 

            if is_left and root.left is None and root.right is None:
                left_sum[0] += root.val

            if root.left is not None:
                bfs(root.left, left_sum, True)

            if root.right is not None:
                bfs(root.right, left_sum, False)

        arr = [0] # for passing as reference
        bfs(root, arr, False)
        return arr[0]


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
