class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        zipped = list(zip(*strs))
        del_col = 0

        print(zipped)

        for col in zipped:
            for i in range(len(zipped[0]) - 1):
                if col[i] > col[i+1]:
                    del_col +=1
                    break



        return del_col
        