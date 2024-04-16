from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        def dfs(root, depth):
            if root is None:
                return

            # if we got the depth we needed
            if depth == 1:

                # store left and right
                left = root.left
                right = root.right

                # set the new node to desired level
                root.left = TreeNode(val)
                root.right = TreeNode(val)

                # Set the left and right of the stored variables
                root.left.left = left
                root.right.right = right

            # if depth not found till yet recurse more to depth !
            dfs(root.left, depth - 1)
            dfs(root.right, depth - 1)

        # if the depth is one meaning make the new node to new root node
        if depth == 1:
            new_node = TreeNode(val, left=root, right=None)
            return new_node

        dfs(root, depth - 1)
        return root


root = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2
Output = [4, 1, 1, 2, None, None, 6, 3, 1, 5]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

Solution().addOneRow(root=root, val=val, depth=depth)
