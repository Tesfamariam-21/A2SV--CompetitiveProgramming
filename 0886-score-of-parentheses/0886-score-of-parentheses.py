class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
            else:
                element = stack.pop()
                if element == "(":
                    stack.append(1)
                else:
                    while stack and stack[-1] != "(":
                        element += stack.pop()
                    stack.pop()                      
                    stack.append(2 * element)
     
        return sum(stack)   
        