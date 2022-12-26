class Solution:
    def freqAlphabets(self, s: str) -> str:
        size = len(s)
        # fastPointer = 2
        slowPointer = 0
        response = []
        message = ""

        
        while slowPointer < len(s):
            if slowPointer + 2 < len(s) and s[slowPointer + 2] == '#':
                message = int(s[slowPointer:slowPointer + 2])
                response.append(chr(message + 96))
                slowPointer += 3
            else:
                message = int(s[slowPointer])
                response.append(chr(message + 96))
                slowPointer += 1
        
        return ''.join(response)
            
                
        
        