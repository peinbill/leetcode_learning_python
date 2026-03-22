from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = list()
        current = head
        while current:
            val_list.append(current.val)
            current = current.next
        left,right = 0,len(val_list)-1
        while left<=right:
            if val_list[left] != val_list[right]:
                return False
            left += 1
            right -= 1

        return True