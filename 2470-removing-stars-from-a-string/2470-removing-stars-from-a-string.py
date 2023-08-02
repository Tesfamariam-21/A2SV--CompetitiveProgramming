class Solution:
    def removeStars(self, s):
        stack = []
        for i in range(0, len(s)):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)