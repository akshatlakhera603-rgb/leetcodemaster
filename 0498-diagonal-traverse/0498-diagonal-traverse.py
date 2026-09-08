class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        level=[0]*m*n
        row=0
        col=0
        up=True
        for i in range (m*n):
            level[i]=mat[row][col]
            if up ==True:
                row-=1
                col+=1
            else:
                row+=1
                col-=1
            if col == n:
                col = n - 1
                row += 2
                up = False
            


            if row == m:
                row=m-1
                col+=2
                up=True
            

            if row < 0 :
                row = 0
                up = False
            

            if col < 0 :
                col = 0
                up = True
        
        return level
        
        