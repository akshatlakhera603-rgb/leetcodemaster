# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        count=1
        current=head
        while count<left:
            prev=current
            current=current.next
            count+=1
        ref=prev
        temp=current
        while count<right:
            current=current.next
            count+=1
        temp2=current
        ref2=current.next
        prev_node = ref2
        curr = temp

        for i in range(right-left+1):
            nextnode = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = nextnode
        ref.next=prev_node
        return dummy.next

        