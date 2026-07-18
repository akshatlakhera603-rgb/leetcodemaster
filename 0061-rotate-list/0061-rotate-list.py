# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        length=1
        temp=head
        while temp.next!=None:
            temp=temp.next
            length+=1
        
        k=k%length
        if k==0:
            return head
        temp.next=head
        count=length-k-1
        temp=head
        while count>0:
            temp=temp.next
            count-=1
        head=temp.next
        temp.next=None
        
        return head

        