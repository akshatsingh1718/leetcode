from typing import *


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return self.val


class Solution:
    '''
    Runtime
    Details
    70ms
    Beats 43.94%of users with Python3
    Memory
    Details
    18.11MB
    Beats 37.40%of users with Python3
    '''
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        queue = []

        queue.append([root])

        while len(queue) > 0:
            first = queue.pop(0)

            # set the next to the right element of the array
            for i, f in enumerate(first):
                if i + 1 == len(first):
                    break

                f.next = first[i + 1]

            print([f.next for f in first])

            temp_queue = []

            for n in first:
                if n.left is not None:
                    temp_queue.append(n.left)

                if n.right is not None:
                    temp_queue.append(n.right)

            if len(temp_queue) > 0:
                queue.append(temp_queue)


def main():
    node = Node(1)

    node.left = Node(2)
    node.left.left = Node(4)
    node.left.right = Node(5)

    node.right = Node(3)
    node.right.left = Node(6)
    node.right.right = Node(7)

    s = Solution()
    s.connect(node)


if __name__ == "__main__":
    main()
