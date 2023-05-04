class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countWords = Counter(words)
        heap = []
        res = []

        for key, val in countWords.items():
            countWords[key] *=-1

        for key, val in countWords.items():
            heappush(heap, (val, key))

        for _ in range(k):
            res.append(heappop(heap)[1])
           
        return res