class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        gcf = list(c.values())[0]

        for i in c.values():
            gcf = math.gcd(gcf, i)

        return gcf>1