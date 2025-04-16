class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"

        stack = []

        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -=1            
            stack.append(n)

        while k and stack:
            stack.pop()
            k -=1
        
        stack = "".join(stack).lstrip("0")
        
        return stack if stack else "0"
        