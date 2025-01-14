class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dict_ = defaultdict(set)
        res = [0]*len(A)

        for i in range(len(A)):
            count = 0
            if A[i] == B[i]:
                count +=1
            if B[i] in dict_["A"]:
                count +=1
            if A[i] in dict_["B"]:
                count +=1
                
            dict_["A"].add(A[i])
            dict_["B"].add(B[i])

            res[i] = res[i-1] + count


        return res


        