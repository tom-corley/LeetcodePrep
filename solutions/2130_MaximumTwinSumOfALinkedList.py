from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Make a reverse copy of the tree
        prev = None
        cursor = head
        length = 0
        while cursor:
            length += 1
            curr = ListNode(cursor.val)
            curr.next = prev
            cursor = cursor.next
            prev = curr
        rev_head = curr

        # Find maximum twin sum
        mx = 0
        cursor1 = head
        cursor2 = rev_head
        i = 1
        while i <= length / 2:
            twin_sum = cursor1.val + cursor2.val
            if twin_sum > mx:
                mx = twin_sum
            cursor1 = cursor1.next
            cursor2 = cursor2.next
            i += 1 
        return mx