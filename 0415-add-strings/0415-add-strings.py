class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        stack1=[]
        stack2=[]
        carry=0
        for i in num1:
            stack1.append(int(i))
        for i in num2:
            stack2.append(int(i))
        ans = ""

        while stack1 or stack2 or carry:

            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            ans = str(digit) + ans

        return ans