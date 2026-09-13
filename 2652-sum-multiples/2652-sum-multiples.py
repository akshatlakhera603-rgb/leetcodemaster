class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result=0
        while n!=0:
            if n%3==0 or n%5==0 or n%7==0:
                result+=n
            n-=1
        return result        