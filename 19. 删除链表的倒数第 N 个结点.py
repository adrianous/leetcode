# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        x = 0
        while fast and x < n:
            x += 1
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
