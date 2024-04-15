from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], running_sum, global_sum: List[int]):
            if root is not None:

                curr_val = root.val + (running_sum * 10)

                if root.left is None and root.right is None:
                    global_sum[0] += curr_val

                dfs(root.left, curr_val, global_sum)
                dfs(root.right, curr_val, global_sum)

        global_sum = [0]
        dfs(root, 0, global_sum)
        return global_sum[0]


class Solution2:
    # Removing extra memory variables from Solution1
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], running_sum):
            if not root:
                return 0

            running_sum = root.val + (running_sum * 10)

            # only return the sum when we are at the leaf node
            if root.left is None and root.right is None:
                return running_sum

            return dfs(root.left, running_sum) + dfs(root.right, running_sum)

        return dfs(root, 0)


if __name__ == "__main__":
    # TS1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    output = 25

    # TS2
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    output = 1026

    # TS3
    # root = TreeNode(1)
    # root.left = TreeNode(0)
    # output = 10

    print(Solution().sumNumbers(root))
