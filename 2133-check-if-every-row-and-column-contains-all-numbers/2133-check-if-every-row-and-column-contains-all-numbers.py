class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        sum1 = n * (n + 1) // 2

        for i in range(n):
            sum2 = 0
            seen=set()
            for j in range(n):
                sum2 += matrix[i][j]
                seen.add(matrix[i][j])

            if sum2 != sum1 or len(seen)!=n:
                return False

        for j in range(n):
            sum2 = 0
            seen=set()
            for i in range(n):
                sum2 += matrix[i][j]
                seen.add(matrix[i][j])

            if sum2 != sum1 or len(seen)!=n:
                return False

        return True