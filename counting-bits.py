class Solution:
    def countBits(self, n: int) -> List[int]:
        n = n +1 
        ans = []
        
        for i in range(n):
            oneBits = 0

            while i > 0:
                oneBits += i&1
                i = i >> 1

            ans.append(oneBits)

        return ans
        
        # for i in range(n):
        #     ans[i] = list(bin(i)).count("1")

        # return ans


        # def convertToBinary(i, answer):
        #     if i == 0:
        #         return answer

        #     answer += str(i%2)
        #     return convertToBinary(i//2, answer)

        # for i in range(n):
        #     ans[i] = convertToBinary(i, "").count("1")

        # return ans