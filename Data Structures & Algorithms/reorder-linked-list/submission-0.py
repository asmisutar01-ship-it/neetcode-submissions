# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next 
            p2 = p2.next.next 
            
        r = None 
        n = p1.next 
        p1.next = None
        while n :
            t = n.next
            n.next = r 
            r=n
            n=t 

        l = head 
        l1 = r
        while l1 :
            t1 = l.next 
            t2 = l1.next 

            l.next = l1
            l1.next = t1 

            l = t1 
            l1 = t2 


        
         