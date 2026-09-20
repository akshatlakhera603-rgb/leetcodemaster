from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x=-x
        stack=deque([])
        while x!=0:
            rem=x%10
            stack.append(rem)
            x//=10
        ans=0
        while stack:
            ans=ans*10+stack.popleft()
        ans*=sign
        if ans < -(2**31) or ans > 2**31 - 1:
            return 0
        return ans