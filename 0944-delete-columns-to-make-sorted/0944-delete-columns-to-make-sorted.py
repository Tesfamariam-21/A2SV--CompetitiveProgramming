class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_col = 0
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if (j + 1) < len(strs) and ord(strs[j][i]) > ord(strs[j+1][i]):
                    deleted_col += 1
                    break
                    # print(strs[j][i], strs[j+1][i])
                
                
        return deleted_col