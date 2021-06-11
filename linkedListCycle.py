# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # the famous hare and tortoise problem
        torT = hare = head
        
        while(hare and torT and hare.next):
            hare = hare.next.next
            torT = torT.next
            
            if(hare == torT):
                return True
            
        return False
        
