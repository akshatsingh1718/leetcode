class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListFactory:
    def __init__(self):
        pass

    def createNodes(vector):
        prv_node = None
        for i, val in enumerate(vector[::-1]):
            prv_node = ListNode(val, prv_node)
        return prv_node


_TestCases = [[1, 2, 3, 4, 5], [1], [4, 4, 3]]
TestCases = [ListFactory.createNodes(l) for l in _TestCases]

_Expected = [[5, 4, 3, 2, 1], [1], [3, 4, 4]]
Expected = [ListFactory.createNodes(l) for l in _Expected]


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
