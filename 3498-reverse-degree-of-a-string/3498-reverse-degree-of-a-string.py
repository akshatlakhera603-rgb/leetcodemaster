class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            pos = ord('z')-ord(s[i]) + 1
            ans += pos * (1 + i)
        return ans