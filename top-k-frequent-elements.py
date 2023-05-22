class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sortedCounter = dict(sorted(c.items(), key=lambda x:-x[1]))
        ans = []
        for i, v in sortedCounter.items():
            if k > 0 and i not in ans:
                ans.append(i)
                k -= 1
                
        return ans