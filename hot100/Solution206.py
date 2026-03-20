from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        current = head

        while current and current.next:
            next = current.next
            next_next = next.next

            current.next = next_next
            next.next = dummy.next
            dummy.next = next

        return dummy.next