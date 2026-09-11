# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        curr=head
        while curr:
            stack.append(curr.val)
            curr=curr.next
        carry=0
        head=None
        while stack or carry:
            val=stack.pop() if stack else 0
            total=val*2+carry
            digit=(total%10)
            carry=(total//10)
            new = ListNode(digit)
            new.next = head
            head = new

        return head
        