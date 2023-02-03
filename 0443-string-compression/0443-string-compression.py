class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        charCount = 0
        
        if len(chars) == 1:
            return len(chars)
        
        while right < len(chars):
            if chars[left] == chars[right]:
                right += 1
                charCount += 1
            elif chars[left] != chars[right]:
                charList = [str(x) for x in str(charCount)]
                if charCount == 1:
                    left += 1
                else:
                    toBeAdded = [chars[left]] + charList
                    chars[left:right] = toBeAdded
                    left = left+2
                    right = left
                charCount = 0
        charList = [str(x) for x in str(charCount)]
        if charCount != 1:
            chars[left+1:right] = charList        
        
        return len(chars)