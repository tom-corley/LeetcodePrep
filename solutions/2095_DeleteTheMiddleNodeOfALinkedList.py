from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if not head.next:
            return None

        # Slow and Fast pointer to find middle node
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        
        # If the middle node is the end set tail to 0, o/w set it to list after middle
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return head
