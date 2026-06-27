# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        l1 = head 
        while l1 and l1.next :
            l = l.next 
            l1 = l1.next.next
            if l == l1 :
                return True 

        return False 

        