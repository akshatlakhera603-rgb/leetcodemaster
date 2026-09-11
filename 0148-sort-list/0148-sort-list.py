class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        curr = head
        for val in arr:
            curr.val = val
            curr = curr.next

        return head