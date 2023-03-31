class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        res = []

        for n in num[2:]:
            if n == "0":
                a = "1"
            else:
                a = "0"
            res.append(a)
            
        return int("".join(res), 2)