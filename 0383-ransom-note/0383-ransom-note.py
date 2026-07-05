class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        
        for i in magazine:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in ransomNote:
            if j in dic and dic[j]!=0:
                dic[j]-=1
                
            else:
                return False
        
        return True        