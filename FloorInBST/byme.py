class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findFloor(root, X, smallest_diff, floor):
    if root is None:
        return

    print("=" * 20)
    print(f"Root= {root.data}")
    print(f"{smallest_diff =}")
    print(f"{floor =}")

    if root.data <= X and X - root.data < smallest_diff[0]:
        floor[0] = root.data
        smallest_diff[0] = X - root.data

    print(f"New {smallest_diff =}")
    print(f"New {floor =}")

    findFloor(root.left, X, smallest_diff, floor)

    findFloor(root.right, X, smallest_diff, floor)

def floorInBST(root, X):
    if root is None:
        return


    floor = [-1]
    findFloor(root, X, [float("inf")], floor)
    return floor[0]


def main():
    node = TreeNode(10)

    node.left = TreeNode(5)
    node.left.left = TreeNode(2)
    node.left.right = TreeNode(6)

    node.right = TreeNode(15)
    # node.right.left = TreeNode(6)
    # node.right.right = TreeNode(7)
    '''
                 1
        2                   3
    4       5           6       7
    '''


    print(floorInBST(node, X= 8))


if __name__ == "__main__":
    main()
