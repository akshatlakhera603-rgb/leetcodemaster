class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        arr=[]
        for i in range(m):
            minval=float("inf")
            for j in range(n):
                minval=min(minval,matrix[i][j])
            arr.append(minval)
        ans=[]
        for j in range(n):
            maxval=float("-inf")
            for i in range(m):
                maxval=max(maxval,matrix[i][j])
            if maxval in arr:
                ans.append(maxval)

        return ans