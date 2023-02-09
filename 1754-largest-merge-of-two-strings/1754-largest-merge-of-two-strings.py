class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        firstWord = list(word1)
        secondWord = list(word2)

        res = []

        while firstWord and secondWord:
            if firstWord > secondWord:
                res.append(firstWord.pop(0))
            else:
                res.append(secondWord.pop(0))
				

        return "".join(res + firstWord + secondWord)