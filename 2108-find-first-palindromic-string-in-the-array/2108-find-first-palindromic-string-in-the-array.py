class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def solve(s):
            if s ==s[::-1]:
                return True
            else:
                return False
        for i in words:
            if solve(i)==True:
                return i
        return ""
        