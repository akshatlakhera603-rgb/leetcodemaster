class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        arr = [len(s)] * len(s)

        for i in range(len(s)):
            if s[i] == c:
                arr[i] = 0

        idx = -1

        # left -> right
        for i in range(len(s)):
            if arr[i] == 0:
                idx = i
            elif idx != -1:
                arr[i] = i - idx

        idx = -1

        # right -> left
        for i in range(len(s) - 1, -1, -1):
            if arr[i] == 0:
                idx = i
            elif idx != -1:
                arr[i] = min(arr[i], idx - i)

        return arr