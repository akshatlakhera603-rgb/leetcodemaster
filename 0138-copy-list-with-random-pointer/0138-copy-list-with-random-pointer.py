"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        dic={}
        temp=head
        while temp!=None:
            dic[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp!=None:
            dic[temp].next=dic.get(temp.next)
            dic[temp].random=dic.get(temp.random)
            temp=temp.next
        return dic[head]
            
        