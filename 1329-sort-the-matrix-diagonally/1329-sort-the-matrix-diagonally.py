class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        def sort(i,j):
            arr=[]
            while i < m and j <n:
                arr.append(mat[i][j])
                i+=1
                j+=1
            arr.sort()
            i-=len(arr)
            j-=len(arr)
            k=0
            while i <m and j<n:
                mat[i][j]=arr[k]
                k+=1
                i+=1
                j+=1
        for j in range(n):
            sort(0,j)
        for i in range(1,m):
            sort(i,0)
        return mat
        