class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for s in sentences:
            words = s.count(" ") + 1
            maxi = max(maxi, words)
        return maxi
        