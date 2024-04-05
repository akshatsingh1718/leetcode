from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
        -10
       /    \
      9      20
            /   \
          15     7

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

"""

"""
Runtime
Details
73ms
Beats 90.50%of users with Python3
Memory
Details
23.79MB
Beats 85.65%of users with Python3
"""


class Solution:
    def findSum(self, root, current_max):
        if root == None:
            # if we are at the end the just return 0 to not change anything in the parent sum value
            return 0

        # get the left sum and right sum
        # Note: This is the sum excluding the parent value
        # So below are the values of a node left and right side
        left_node_sum = self.findSum(root.left, current_max)
        right_node_sum = self.findSum(root.right, current_max)

        # Now we can make 3 sums from left and right sum of the node
        # left node sum with the parent value
        # right node sum with the parent value
        # both left and right nodes with parent value
        l_node_with_curr = left_node_sum + root.val
        r_node_with_curr = right_node_sum + root.val
        both_node_with_curr = left_node_sum + right_node_sum + root.val

        # get the current stage max value
        # This is the value which will be returned to the parent of the current node
        # Why only comparing current node value, left node sum with curr node value and right node sum with curr node value ?
        # Because we want to return only the straight branches of the parent that are going down and not considering
        # both the branches of the parent and only to consider one branch or only its child node value
        curr_stage_max = max(root.val, l_node_with_curr, r_node_with_curr)

        # here we are getting the max of curr_stage_max with and both nodes summed with curr node value as the
        # max value could be determined by the both branches combined and not considering the parent value of the
        # curr node
        current_max[0] = max(current_max[0], both_node_with_curr, curr_stage_max)

        # Debugging
        # print("-" * 20)
        # print(f"Root= {root.val}")
        # print(f"{left_node_sum = }")
        # print(f"{right_node_sum = }")
        # print(f"{l_node_with_curr = }")
        # print(f"{r_node_with_curr = }")
        # print(f"{both_node_with_curr = }")
        # print(f"{current_max = }")
        # print(f"Return {curr_stage_max}")

        # here return the max of one of the branches of the curr node
        return curr_stage_max


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
