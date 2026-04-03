class Solution:
    def alternateDigitSum(self, n: int) -> int:
        rev=0
        while n !=0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        sum=0
        pos=1
        while rev!=0:
            rem1=rev%10
            if pos % 2 != 0:    
                sum += rem1
            else:               
                sum -= rem1

            pos += 1            
            rev //= 10
        return sum


        