from typing import List, Optional
from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListFactory:
    def createNodes(vector: List[int]):
        prv_node = None
        for i, val in enumerate(vector[::-1]):
            prv_node = ListNode(val, prv_node)
        return prv_node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    TC: O(n)
    SC: (depth of the tree)
    '''
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if root.left is None or root.right is None:
            return root.val

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        return left_val | right_val if root.val == 2 else left_val & right_val


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)


output = True
print(Solution().evaluateTree(root))
