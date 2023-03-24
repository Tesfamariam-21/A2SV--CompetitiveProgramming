class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(arr, index, count):
            if count == 4 and index == len(s):
                res.append(arr[:-1])
                return

            elif count > 4:
                return 

                # print(arr)
            
            for i in range(index, min(index + 3,len(s))):
                if int(s[index:i+1]) < 256 and (i - index == 0 or s[index] != "0"):
                    backtrack(arr + s[index:i+1] + ".", i + 1, count + 1)


        backtrack("", 0, 0)
        return res