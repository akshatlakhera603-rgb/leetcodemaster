# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        decimal=0
        arr.reverse()
        for i in range(len(arr)):
            decimal+=arr[i]*(2**i)
        return decimal

        