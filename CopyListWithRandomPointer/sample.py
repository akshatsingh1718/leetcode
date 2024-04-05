class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class ListFactory:
    def __init__(self):
        pass

    def createNodes(vector):
        prv_node = None
        n = len(vector)
        nodes_list = [None] * (n)

        # create normal list
        for i, (val, random) in enumerate(vector[::-1]):
            prv_node = Node(val, prv_node)
            nodes_list[n - 1 - i] = prv_node

        # set the random nodes reference
        for node_i, (_, random_idx) in zip(nodes_list, vector):
            if random_idx is not None:
                node_i.random = nodes_list[random_idx]
            else:
                node_i.random = None

            nodes_list

        return prv_node


_TestCases = [[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]]
TestCases = [ListFactory.createNodes(l) for l in _TestCases]


def isListsSame(head1: Node, head2: Node):
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:
            if head1.random is not None and head2.random is not None:
                if head1.random.val != head2.random.val:
                    return  False
            else:
                return False
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def getList(head: Node) -> list:
    nlist = []
    while head is not None:
        nlist.append([head.val, head.random.val if head.random else head.random])
        head = head.next

    return nlist
