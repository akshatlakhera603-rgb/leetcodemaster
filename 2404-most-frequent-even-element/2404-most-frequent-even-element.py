class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq={}
        count=0
        for i in nums:
            if i%2==0:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
        if len(freq) == 0:
            return -1
        ans=-1
        for key in freq:
            if freq[key] > count or (freq[key] == count and key < ans):
                count = freq[key]
                ans = key
        return ans
        

        