class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    lstr = ""
    while head is not None:
        lstr += str(head.val) + ", "
        head = head.next
        i += 1

    return lstr


class ListFactory:
    def __init__(self):
        pass

    def createNodes(vector, idx_to_join, isJoin):
        prv_node = None

        n = len(vector)

        join_node = None
        last_node = None

        for i, val in enumerate(vector[::-1]):
            prv_node = ListNode(val, prv_node)

            if i == 0:
                last_node = prv_node

            if n - idx_to_join == i and isJoin:
                join_node = prv_node

        last_node.next = join_node

        return prv_node


_TestCases = [([9, 10, 11, 12, 13], 10, False), ([1, 2, 3, 4, 5, 6], 2, True)]
TestCases = [(ListFactory.createNodes(*l), l[2]) for l in _TestCases]


def isListsSame(list1, list2):
    head1, head2 = list1, list2
    while (head1 != None) or (head2 != None):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return True
