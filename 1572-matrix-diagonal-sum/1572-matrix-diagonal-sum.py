class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m=len(mat)
        sum1=0
        sum2=0
        total=0
        for i in range (m):
            sum1+=mat[i][i]
            sum2+=mat[i][m-1-i]
        if m%2!=0:
            total+=sum1+sum2-mat[m//2][m//2]
        else:
            total+=sum1+sum2
        return total            
        