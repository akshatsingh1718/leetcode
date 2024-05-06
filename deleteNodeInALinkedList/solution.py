'''
Problem: https://leetcode.com/problems/delete-node-in-a-linked-list/?envType=daily-question&envId=2024-05-05
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next
        # node.val, node.next = node.next.val, node.next.next