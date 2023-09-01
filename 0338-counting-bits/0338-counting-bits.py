class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i&1)
        
        return ans
            
        
        # for i in range(n):
        #     oneBits = 0

        #     while i > 0:
        #         oneBits += i&1
        #         i = i >> 1

        #     ans.append(oneBits)

        # return ans
        
        # for i in range(n):
        #     ans[i] = list(bin(i)).count("1")

        # return ans


        # def convertToBinary(i):
        #     if i == 0:
        #         return 0

        #     return i%2 + convertToBinary(i//2)

        # for i in range(n):
        #     ans[i] = convertToBinary(i)

        # return ans

        
        
