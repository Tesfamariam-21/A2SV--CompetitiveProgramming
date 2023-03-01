class Solution:
    def decodeString(self, s: str) -> str:
        if s.isnumeric():
            return ""
        if "[" not in s:
            return s
        
        def decode(s,index, stack):
          
            
            if index == len(s):
                return 
            elif s[index].isdigit():
                stack.append(s[index])
                return decode(s, index+1, stack)
            elif s[index] == '[':
                stack.append('[')
                return decode(s, index+1, stack)
            elif s[index] == "]":
                temp = ""
                num = ""
                
                while stack[-1] != "[":
                    temp +=stack.pop()
                    if not stack:
                        break
                temp = temp[::-1]
                stack.pop()
                
                while stack[-1] != "[":
                    if stack[-1].isnumeric():
                        num += stack.pop()
                    else:
                        break
                    if not stack:
                        break
             
                num = num[::-1]
                num = int(num)
                temp = num* temp
                stack.append(temp[::-1])
                return decode(s, index + 1, stack)
            else:
                stack.append(s[index])
                return decode(s, index + 1, stack)
        
        stack = []
        decode(s, 0, stack)
        ans = ""
        for i in stack:
            ans += i[::-1]

        return "".join(ans)