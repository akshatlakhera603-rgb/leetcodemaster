# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        node=ListNode(0)
        head=node
        while temp1!= None and temp2!=None:
            if temp1.val>=temp2.val:
                node.next=temp2
                temp2=temp2.next
                node=node.next
            else:
                node.next=temp1
                temp1=temp1.next
                node=node.next
        while temp1:
            node.next=temp1
            temp1=temp1.next
            node=node.next
        while temp2:
            node.next=temp2
            temp2=temp2.next
            node=node.next
        return head.next       

        