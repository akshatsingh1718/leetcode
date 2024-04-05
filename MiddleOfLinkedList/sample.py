class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    lstr = ""
    while head is not None:
        lstr += str(head.val) + ", "
        head = head.next
    return lstr


class ListFactory:
    def __init__(self):
        pass

    def createNodes(vector):
        prv_node = None

        n = len(vector)
        flag = n // 2

        middle_node = None

        for i, val in enumerate(vector[::-1]):
            prv_node = ListNode(val, prv_node)

        middle_node = prv_node
        while flag > 0:
            middle_node = middle_node.next
            flag -= 1

        return prv_node, middle_node


_TestCases = [[1, 2, 3, 4, 5, 6], [1], [4, 5, 6]]
TestCases = [ListFactory.createNodes(l) for l in _TestCases]


def isListsSame(list1, list2):
    head1, head2 = list1, list2
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:

            return False
        head1 = head1.next
        head2 = head2.next

    return True
