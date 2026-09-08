class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat1=[[0 for _ in range (len(colSum))] for _ in range (len(rowSum))]

        for i in range(len(rowSum)):
            for j in range (len(colSum)):
                mini=min(rowSum[i],colSum[j])
                mat1[i][j]=mini
                rowSum[i]-=mini
                colSum[j]-=mini
        return mat1
        