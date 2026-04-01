class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxf=max(freq.values())
        count=0
        for keys in freq:
            if freq[keys]==maxf:
                count+=freq[keys]

        return count
         
        