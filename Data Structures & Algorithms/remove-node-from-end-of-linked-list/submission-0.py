# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = None 
        l = head 
        while l :
            t = l.next 
            l.next = r 
            r = l
            l = t 

        i = 1
        curr = r
        if n == 1:
            r = r.next
        else:
            while curr and curr.next:
                if i == n - 1:
                    curr.next = curr.next.next
                    break
                curr = curr.next
                i += 1
                
        r1 = None 
        l1 = r
        while l1 :
            t = l1.next 
            l1.next = r1 
            r1 = l1
            l1 = t  
        return r1       



                