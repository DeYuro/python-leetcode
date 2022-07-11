from typing import Optional
from problems.structures.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mem = 0
        ans = ListNode()
        head = ans
        while l1 is not None or l2 is not None or mem > 0:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            sum +=mem

            mem = sum // 10

            ans.next = ListNode(val=round(sum % 10))
            ans = ans.next
        return head.next