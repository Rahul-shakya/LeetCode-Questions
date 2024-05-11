# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        len = 0
        while(curr != None):
            len += 1
            curr = curr.next
        targetN = len - n
        if(targetN == 0):
            return head.next
        i = 0
        prev = head
        curr = head
        while(i < targetN):
            prev = curr
            curr = curr.next
            i += 1
        prev.next = prev.next.next
        return head
