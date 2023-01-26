class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOfIndex={}
        answer = []
        for i in range(len(s)):
            lastOfIndex[s[i]]=i
        print(lastOfIndex)
        
        
        left = 0
        right = 0
        while left < len(s):
            temp = lastOfIndex[s[left]]
            while right < temp:
                lastIndex = lastOfIndex[s[right]]
                if lastIndex > temp:
                    temp = lastIndex
                right += 1
            answer.append((right - left) + 1)
            right += 1
            left = right
            
        return answer