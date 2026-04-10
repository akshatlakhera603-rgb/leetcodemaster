class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while True:
            if n==2**i:
                return True
            if 2**i>n:
                return False
            i+=1