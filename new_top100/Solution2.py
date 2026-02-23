from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_number(l1, l2, add_one=False):
            if l1 is None and l2 is None:
                if add_one:
                    return ListNode(val=1)
                else:
                    return None

            if l1 is None:
                if add_one:
                    if l2 == 9:
                        value = 0
                        next = add_number(None, l2.next, add_one=True)
                    else:
                        value = l2.val + 1
                        next = add_number(None, l2.next, add_one=False)
                        if value >= 10:
                            value = value % 10
                            next = add_number(None, l2.next, add_one=True)


                else:
                    value = l2.val
                    next = add_number(None, l2.next, add_one=False)
                return ListNode(val=value, next=next)

            if l2 is None:
                if add_one:
                    if l1 == 9:
                        value = 0
                        next = add_number(l1.next, None, add_one=True)
                    else:
                        value = l1.val + 1
                        if value >= 10:
                            value = value % 10
                            next = add_number(l1.next, None, add_one=True)
                        else:
                            next = add_number(l1.next, None, add_one=False)

                else:
                    value = l1.val
                    next = add_number(l1.next, None, add_one=False)
                return ListNode(val=value, next=next)

            if add_one:
                l3_val = l1.val + l2.val + 1
            else:
                l3_val = l1.val + l2.val

            next = add_number(l1=l1.next, l2=l2.next, add_one=True if l3_val >= 10 else False)

            if l3_val >= 10:
                l3_val = l3_val % 10

            return ListNode(val=l3_val, next=next)

        return add_number(l1, l2, add_one=False)