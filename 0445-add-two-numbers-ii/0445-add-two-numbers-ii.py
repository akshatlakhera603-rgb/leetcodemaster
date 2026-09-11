# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = l1

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        l1=prev
        prev = None
        curr = l2

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        l2=prev
        dummy=ListNode(0)
        l3=dummy
        temp=l1
        temp1=l2
        carry=0
        while temp or temp1 or carry:
            val1=temp.val if temp else 0
            val2=temp1.val if temp1 else 0
            total=val1+val2+carry
            carry=(total//10)
            total=(total%10)
            l3.next=ListNode(total)
            l3=l3.next

            if temp:
                temp=temp.next
            if temp1:
                temp1=temp1.next
        prev=None 
        curr=dummy.next
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

        

        

        
        