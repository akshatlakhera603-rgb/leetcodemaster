class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        for j in range(k):
            if s[j] in "aeiou":
                count+=1
        i=0
        maxcount=count
        for j in range(k,len(s)):
            if s[i] in "aeiou":
                count-=1
            i+=1
            if s[j] in "aeiou":
                count+=1
            maxcount=max(maxcount,count)
        return maxcount            
            

        