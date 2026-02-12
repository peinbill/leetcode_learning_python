from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next
        slow = head
        while fast and slow:
            if fast is slow:
                return True
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False

        return False