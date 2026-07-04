class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i in dic1:
                    dic1[i]+=1
                else:
                    dic1[i]=1
            for j in t:
                if j in dic1:
                    dic1[j]-=1
                else:
                    return False
        for value in dic1.values():
            if value != 0:
                return False

        return True
          