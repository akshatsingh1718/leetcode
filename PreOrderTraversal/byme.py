from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def traversal(root):
    if root is None:
        return None

    print(root.val)

    traversal(root.left)
    traversal(root.right)


def main():
    node = TreeNode(1)

    node.left = TreeNode(2)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)

    node.right = TreeNode(3)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)

    traversal(node)


if __name__ == "__main__":
    main()
