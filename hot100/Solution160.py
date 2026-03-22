class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current_a_dict = set()
        current_a = headA
        while current_a:
            current_a_dict.add(current_a)
            current_a = current_a.next

        current_b = headB
        while current_b:
            if current_b in current_a_dict:
                return current_b
            current_b = current_b.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

