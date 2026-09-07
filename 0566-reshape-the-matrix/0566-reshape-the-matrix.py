class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        mat1=[[0 for _ in range(c)] for _ in range(r)]
        arr=[0]*(m*n)
        k=0
        if m*n != r*c:
            return mat
       
        for i in range(m):
            for j in range(n):
                arr[k]=mat[i][j] 
                k+=1
                
        k=0
        for i in range(r):
            for j in range(c):
                mat1[i][j]=arr[k]
                k+=1
        return mat1
       

        