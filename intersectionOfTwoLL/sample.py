class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListFactory:
    def __init__(self):
        pass

    @staticmethod
    def createNodes(vector):
        prv_node = None
        for i, val in enumerate(vector[::-1]):
            prv_node = ListNode(val, prv_node)
        return prv_node

    @staticmethod
    def createConnectedLists(vector1, vector2, idxToConnect):
        list1 = ListFactory.createNodes(vector1)
        list2 = ListFactory.createNodes(vector2)

        if idxToConnect < 0:
            return list1, list2, None

        # find the nth element of the list2
        curr2 = list2
        for i in range(idxToConnect):
            curr2 = curr2.next

        tail1 = list1
        # if list1 is not none meaning list is not empty
        if list1 is not None:
            # get tail of list1
            while tail1.next is not None:
                tail1 = tail1.next

            # Now set tail1.next to the nth element of the list2
            tail1.next = curr2
        else:  # if list2 is empty
            list1 = curr2

        return list1, list2, curr2


# list1, list2, idx of list2 will be the next for list1 end node
_TestCases = [
    ([4, 1], [5, 6, 1, 8, 4, 5], 3),
    ([3], [1, 9, 1, 2, 4], 3),
    ([2, 6, 4], [1, 5], -1),
    ([], [1], 0),
]
TestCases = [ListFactory.createConnectedLists(*l) for l in _TestCases]


def isListsSame(list1, list2):
    head1, head2 = list1, list2
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def printList(head):
    lstr = ""
    while head is not None:
        lstr += str(head.val) + ", "
        head = head.next
    return lstr