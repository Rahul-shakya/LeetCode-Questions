# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        fwd = curr = head
        prev = None
        while fwd != None:
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
            
        return prev
            
        
