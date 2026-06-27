class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        alpha=""
        out=-1
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in freq:
            if freq[j]==1:
                alpha=j
                break
        for x in range(len(s)):
            if s[x]==alpha:
                out=x
        return out



        