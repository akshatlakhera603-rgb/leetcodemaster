class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        for j in arr:
            dic[j]=dic.get(j,0)+1
        maxans=-1
        for i in dic:
            if dic[i]==i:
                maxans=max(i,maxans)
        return maxans
        
        