class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        costtotal=0
        for i in range(len(gas)):
            total+=gas[i] 
        for j in range (len(cost)):
            costtotal+=cost[j]
        if total<costtotal:
            return -1
        indice=0
        start=0
        i=0
        j=len(gas)
        while i<j:
            indice+=gas[i]-cost[i]
            if indice <0:
                start=i+1
                indice=0
                i+=1
            else:
                i+=1
        return start


        