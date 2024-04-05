from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val=}"


class Solution:
    """
    Runtime
    Details
    40ms
    Beats 90.71%of users with Python3
    Memory
    Details
    17.13MB
    Beats 33.85%of users with Python3
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        # use queue
        queue = []

        # arr to store the result
        arr = []

        queue.append([root])
        while len(queue) > 0:
            # print(queue)
            # print(arr)

            first = queue.pop(0)
            
            arr.append([f.val for f in first])

            level_nodes = []

            for node in first:
                    
                if node.left is not None:
                    level_nodes.append(node.left)

                if node.right is not None:
                    level_nodes.append(node.right)

            if len(level_nodes) > 0: queue.append(level_nodes)
        return arr


if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(6)


    s = Solution()
    print(s.levelOrder(root))
