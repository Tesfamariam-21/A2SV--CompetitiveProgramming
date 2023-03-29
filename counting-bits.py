class Solution:
    def countBits(self, n: int) -> List[int]:
        n = n +1 
        ans = [0]* n

        for i in range(n):
            ans[i] = list(bin(i)).count("1")

        return ans