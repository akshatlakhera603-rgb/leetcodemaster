class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        arr=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==2:
                arr.append(i)
        return arr
        