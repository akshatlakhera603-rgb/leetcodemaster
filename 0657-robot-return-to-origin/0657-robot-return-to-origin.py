class Solution:
    def judgeCircle(self, moves: str) -> bool:
        st1=0
        st2=0
        for i in moves:
            if i=="L":
                st1+=1
            elif i=="R":
                st1-=1
            elif i=="U":
                st2+=1
            else:
                st2-=1
        if st1==0 and st2==0:
            return True
        else:
            return False
        