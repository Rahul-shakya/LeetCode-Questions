# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

''' Not the cleanest approach, but in-place code,
    the sum is overwritten in 2nd LinkedList
    Runtime was 60 ms, faster than 96.68% of Python3 online submission'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = l2
        carry = 0
        inL1 = False
        while(l1 and l2):
            curr1 = l1.val
            curr2 = l2.val
            prev1 = l1
            prev2 = l2
            if(curr1 + curr2 + carry) == 10:
                l2.val = 0
            elif (curr1 + curr2 + carry) > 10:
                l2.val = curr1 + curr2  - 10 + carry
            else:
                l2.val = curr1 + curr2 + carry
            l1 = l1.next
            l2 = l2.next
            carry = int((curr1 + curr2 + carry) / 10)

        # the last element of the shorter list is pointed towards the element after the last 
        # one of the bigger list and the summation is continued there
        if(l1):
            prev2.next = l1
        else:
            prev1.next = l2
        while(l1):
            inL1 = True
            prev1 = l1
            tot = l1.val + carry
            l1.val = (tot)%10 
            carry = int(tot / 10)
            l1 = l1.next
        while(l2):
            prev2 = l2
            tot = l2.val + carry
            l2.val = (tot)%10 
            carry = int(tot / 10)
            l2 = l2.next
            
        if(carry == 1):
            if(inL1):
                prev1.next = ListNode(1)
            else:
                prev2.next = ListNode(1)
            
            
        return ans

