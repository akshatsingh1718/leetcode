from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        itos = lambda i: (chr(i + 97))

        def dfs(root, smallest_seq: list, curr_seq:str):
            if root is None:
                return

            curr_seq = f"{itos(root.val)}{curr_seq}"
            if root.left is None and root.right is None:
                smallest_seq[0] = min(smallest_seq[0], curr_seq)
                return

            dfs(root.left, smallest_seq, curr_seq= curr_seq)
            dfs(root.right, smallest_seq, curr_seq= curr_seq)

        
        smallest_seq = ["{"]
        dfs(root, smallest_seq, curr_seq="")
        return smallest_seq[0]


stoi = lambda s: (ord(s) - 97)

root = TreeNode(stoi("z"))
root.left = TreeNode(stoi("b"))
root.right = TreeNode(stoi("d"))

root.left.left = TreeNode(stoi("b"))
root.left.right = TreeNode(stoi("d"))

root.right.left = TreeNode(stoi("a"))
root.right.right = TreeNode(stoi("c"))

print(Solution().smallestFromLeaf(root))