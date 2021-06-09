# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        curr = ListNode(0)
        res = curr
        
        while(l1 and l2):
            
            if(l1.val < l2.val):
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
                
            curr=curr.next

        #appending the remaining list to the merged list, no need to have a while loop

        if(l1):
            curr.next = l1
            
        if(l2):
            curr.next = l2
        
        return res.next
