from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        odd = False
        odd_head = ListNode()
        even_head = ListNode()
        odd_cursor = odd_head
        even_cursor = even_head

        while cursor:
            odd = not odd
            if odd:
                odd_cursor.next = cursor
                odd_cursor = odd_cursor.next
            else:
                even_cursor.next = cursor
                even_cursor = even_cursor.next
            cursor = cursor.next
        odd_cursor.next = even_head.next
        even_cursor.next = None
        return odd_head.next
