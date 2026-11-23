# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # remove the nth node from the front of the reversed list
        if n == 1:
            prev = prev.next          # drop the head
        else:
            curr2 = prev
            x = 1
            while x < n - 1:
                curr2 = curr2.next
                x += 1
            curr2.next = curr2.next.next

        # reverse back
        prev2 = None
        tmp = prev                    # set AFTER the removal
        while tmp:
            nxt = tmp.next
            tmp.next = prev2
            prev2 = tmp
            tmp = nxt

        return prev2