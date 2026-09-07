class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        maxcount=0
        i=0
        ans=[]
        for x in range(m-1,-1,-1):
            count=0
            for j in range(n):
                if mat[x][j]==1:
                    count+=1
                if count>=maxcount:
                    maxcount=count
                    i=x
        ans.insert(0,i)
        ans.insert(1,maxcount)
        return ans

        
        

        