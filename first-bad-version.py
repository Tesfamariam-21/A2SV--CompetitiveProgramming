# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n 
        bad = 0

        while low <= high:
            mid = (high + low)//2

            if isBadVersion(mid) == False:
                low = mid +1
            elif isBadVersion(mid) == True:
                high = mid - 1
                if not isBadVersion(high):
                    return high + 1
   
            else:
                bad = n
                break

        return bad