class Solution:
    def addDigits(self, num: int) -> int:
        sum1=num
        while sum1>=10:
        
            sum1 = sum(int(d) for d in str(sum1))

        return sum1
        