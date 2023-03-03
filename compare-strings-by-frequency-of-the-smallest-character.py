class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queriesNum = []
        wordsNum = []

        for querie in queries:
            queriesNum.append(querie.count(min(querie)))
        
        for i in words:
            wordsNum.append(i.count(min(i)))

        if len(wordsNum) == 1:
            return [1] if queriesNum[0] < wordsNum[0] else [2]

        wordsNum = sorted(wordsNum)

        high = len(wordsNum)
        low = 0
        ans = []
        for i in range(len(queriesNum)):
            ind =bisect_right(wordsNum, queriesNum[i])
            if ind >= len(wordsNum):
                ans.append(0)
            else:
                ans.append(len(wordsNum) - ind)

        return ans