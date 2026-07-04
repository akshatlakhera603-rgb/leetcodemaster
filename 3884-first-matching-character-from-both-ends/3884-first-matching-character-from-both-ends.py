class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        minval=float('inf')
        for i in range(len(s)):
            if s[i]==s[n-i-1]:
                minval=min(minval,i)
        if minval==float('inf'):
            return -1
        return minval

        