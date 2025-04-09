class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for b in s:
            if stack and b in hm and hm[b] == stack[-1]:
                stack.pop()
            else:
                stack.append(b)
        

        return True if not stack else False