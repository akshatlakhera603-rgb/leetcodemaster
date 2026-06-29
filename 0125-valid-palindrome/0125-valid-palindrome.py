class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for ch in s:
            if ch.isalnum():
                word += ch

        word = word.lower()

        word1 = word[::-1]

        if word1 == word:
            return True
        else:
            return False