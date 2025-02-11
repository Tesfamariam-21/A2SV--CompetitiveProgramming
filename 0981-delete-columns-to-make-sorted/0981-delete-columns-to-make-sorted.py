class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_col = 0

        for i in range(len(strs[0])):
            prev = strs[0][i]
            for j in range(1, len(strs)):
                if prev > strs[j][i]:
                    del_col +=1
                    break
                prev = strs[j][i]
        
        return del_col

        # zipped = list(zip(*strs))
        # del_col = 0

        # print(zipped)

        # for col in zipped:
        #     for i in range(len(zipped[0]) - 1):
        #         if col[i] > col[i+1]:
        #             del_col +=1
        #             break



        # return del_col
        