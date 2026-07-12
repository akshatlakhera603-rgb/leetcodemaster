# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=list1
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        temp=list2
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        node = ListNode(0)
        head=node

        for i in arr:
            x=ListNode(i)
            node.next=x
            node=node.next

        return head.next

        