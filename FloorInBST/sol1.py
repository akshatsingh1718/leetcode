class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floorInBST(root, X):
    if root is None:
        return -1

    ans = -1

    leftFloor= floorInBST(root.left, X)
    rightFloor= floorInBST(root.right, X)

    if leftFloor <= rightFloor and rightFloor <= X:
        ans = rightFloor

    if leftFloor > rightFloor and leftFloor <= X:
        ans = leftFloor

    if root.data > ans and root.data <= X:
        ans = root.data 

    return ans


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
