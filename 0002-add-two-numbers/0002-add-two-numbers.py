# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=l1
        temp1=l2
        node=ListNode(0)
        l3=node
        carry=0
        while temp or temp1 or carry:

            val1 = temp.val if temp else 0
            val2 = temp1.val if temp1 else 0    
            total=val1+val2+carry
            
            carry=(total//10)
            total=(total%10)
            l3.next=ListNode(total)
            l3=l3.next
            
            if temp!=None:
                temp=temp.next
            if temp1!=None:
                temp1=temp1.next
        return node.next


            
        