# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        torT = hare = fromHead = head
        
        while(hare and hare.next):
            hare = hare.next.next
            torT = torT.next
            
            if(hare == torT):
                while(hare != fromHead):
                    fromHead = fromHead.next
                    hare = hare.next
                return fromHead
