# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while prev!=None:
            check=prev
            count=0
            while count<k and check.next!=None:
                check =check.next
                count+=1

            if count<k:
                break

            
            groupnext=check.next

            curr=prev.next
            prev_node=groupnext
            
            for i in range(k):
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node
            
            temp=prev.next
            prev.next=prev_node
            prev=temp
        return dummy.next
            