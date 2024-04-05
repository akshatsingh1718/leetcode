from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    """'
    Runtime
    Details
    42ms
    Beats 81.10%of users with Python3
    Memory
    Details
    17.55MB
    Beats 74.56%of users with Python3
    """

    def getLastNode(self, root: Optional[TreeNode]):
        if root is None:
            return None
        while root.right is not None:
            root = root.right

        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        # make the left of all nodes as None
        root.left = None

        # if left is none then make the next value as right of the node
        if left is None:
            root.right = right
        else:
            # if left node is not null then make its next to the curr node
            root.right = left
            # find the last node of the left node
            last_node_of_left = self.getLastNode(left)
            # make the last node of left to be right of the curr
            last_node_of_left.right = right

        # print("=" * 30)
        # print(f"Root= {root}")
        # print(f"right= {right}")
        # print(f"left= {left}")

        return root


def main():
    node = TreeNode(1)

    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)

    node.right = TreeNode(5)
    node.right.right = TreeNode(6)

    s = Solution()

    ll = s.flatten(node)

    while ll is not None:
        print(ll.val, end="->")
        ll = ll.right


if __name__ == "__main__":
    main()
