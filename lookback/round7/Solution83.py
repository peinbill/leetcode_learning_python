
from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        next = dummy.next
        if not next:
            return dummy.next
        next_next = next.next
        if not next_next:
            return dummy.next

        while next and next_next:

            if next.val == next_next.val:
                next.next = next_next.next
                next_next = next_next.next

            else:
                next = next_next
                next_next = next_next.next

        return dummy.next