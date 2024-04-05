from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    """
    Runtime
    Details
    74ms
    Beats 88.64%of users with Python3
    Memory
    Details
    23.93MB
    Beats 18.76%of users with Python3
    """

    def findSum(self, root, current_max):
        if root == None:
            # if we are at the end the just return 0 to not change anything in the parent sum value
            return 0

        left_node_sum = max(0, self.findSum(root.left, current_max))
        right_node_sum = max(0, self.findSum(root.right, current_max))

        current_max[0] = max(current_max[0], left_node_sum + right_node_sum + root.val)

        return root.val + max(left_node_sum, right_node_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        current_max = [float("-inf")]
        self.findSum(root, current_max)
        return current_max[0]


def main():
    # root = TreeNode(2)
    # root.left = TreeNode(-1)
    # root.right = TreeNode(-2)

    """
        -10
       /    \
      9      20
            /   \
          15     -7
    """
    # root = TreeNode(-10)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.right = TreeNode(7)
    # root.right.left = TreeNode(15)

    # [-10]
    root = TreeNode(-10)

    # [1,-2,-3,1,3,-2,null,-1]

    """
              1
           /     \
         -2       -3 
        /   \    /   \
       1     3  -2 
      /
     -1 
    """
    # root = TreeNode(1)
    # root.left = TreeNode(-2)
    # root.right = TreeNode(-3)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(-2)
    # root.right.right = None
    # root.left.left.left = TreeNode(-1)

    # [-1,8,2, null,-9,0,null,null,null,-3,null,null,-9,null,2]

    s = Solution()

    print("Max Sum ", s.maxPathSum(root))


main()
