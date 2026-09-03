class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        maxlen=0
        dic={}
        for right in range(len(fruits)):
            dic[fruits[right]]=dic.get(fruits[right],0)+1

            while len(dic)>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen

        