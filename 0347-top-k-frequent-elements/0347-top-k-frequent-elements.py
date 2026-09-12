class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dics={}
        arr=[0]*k
        for i in nums:
            dics[i]=dics.get(i,0)+1
        sortde=dict(sorted(dics.items(), key=lambda x: x[1], reverse=True))
        i=0
        for key in sortde:
            if i==k:
                break
            arr[i]=key
            i+=1
            
        return arr
        
        
        