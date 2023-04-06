class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0

        def backtrack(bits, index):
            nonlocal ans
            if index == n:
                ans +=1
                return


            for i in range(1, n+1):
                if bits & (1 << (i-1)) == 0:
                    if i % (index + 1) == 0 or (index + 1) % i ==0:
                        backtrack(bits |(1 << (i -1)), index +1)

            # for i in range(1, n+1):
            #     if bits & (1 << (i -1)) == 0:
            #         if i % (index + 1) == 0 or (index + 1) % i ==0:
            #             bits |= (1 << (i -1))
            #             backtrack(bits, index+1)
            #             bits &= ~(1<<i-1)

    
        

        backtrack(0, 0)
        return ans