class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        def toep(i,j):
            arr=[]
            while i<m and j<n:
                if len(arr)!=0 and arr[-1]!=matrix[i][j]:
                    return False
                arr.append(matrix[i][j])
                i+=1
                j+=1
            return True
        for j in range (n):
            if toep(0,j)==False:
                return False
        for i in range(1,m):
            if toep(i,0)==False:
                return False
        return True

        