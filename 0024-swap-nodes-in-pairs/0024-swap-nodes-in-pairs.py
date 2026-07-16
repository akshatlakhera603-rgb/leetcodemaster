# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        
       
        while prev.next !=None and prev.next.next!=None:
            first=prev.next
            second=first.next
            prev.next=second
            first.next=second.next
            second.next=first
            prev=first
        return dummy.next

        
        