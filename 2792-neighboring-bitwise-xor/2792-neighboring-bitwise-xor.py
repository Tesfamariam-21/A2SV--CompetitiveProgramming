class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        arr = [0]

        for i in range(len(derived)):
            if derived[i] ^ arr[i]:
                arr.append(1)
            else:
                arr.append(0)

        return arr[0] == arr[-1]