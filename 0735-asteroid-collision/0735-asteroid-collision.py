class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0 and stack[-1]>0 and stack[-1]<abs(i):
                stack.pop()
            if stack and i<0 and  stack[-1]==abs(i):
                stack.pop()
                continue
           
            
            elif not stack or i > 0 or stack[-1] < 0:
                stack.append(i)
        return stack
            
        
        