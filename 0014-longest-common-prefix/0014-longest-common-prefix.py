class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        st1=strs[0]
        st2=strs[len(strs)-1]
        st=""
        check=True
        for i in range(len(st1)):
            if st1[i]!=st2[i]:
                check=False
                break
            if check==True:
                st+=st1[i]
        return st
            

        
            

        