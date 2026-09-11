# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        result=dummy
        def help(val):
            nonlocal dummy
            dummy.next=ListNode(val)
            dummy=dummy.next
        temp=head
        while temp :
            if temp.val<x:
                help(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.val>=x:
                help(temp.val)
            temp=temp.next
        return result.next


        