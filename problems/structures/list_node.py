from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_from_list(l: Optional[list]) -> Optional[ListNode]:
    result = ListNode()
    head = result

    for v in l:
        result.next = ListNode(v)
        result = result.next

    return head.next
