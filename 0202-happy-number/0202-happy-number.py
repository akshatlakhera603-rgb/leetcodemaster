class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True 
        if n<10:
            return False
        sum1=0
        while n!=0:
            rem=n%10
            sum1+=rem*rem
            n//=10
        return self.isHappy(sum1)
                