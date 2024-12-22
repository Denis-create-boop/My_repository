# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Step 2: Handle cases where k >= length
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the breaking point
        breakPoint = length - k
        current = head
        for _ in range(breakPoint - 1):
            current = current.next

        # Step 4: Rotate the list
        new_head = current.next
        current.next = None
        tail.next = head

        return new_head
