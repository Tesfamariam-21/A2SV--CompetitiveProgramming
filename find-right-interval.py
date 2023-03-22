class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dict_ = {}
        ans = []
        flag = True
        if len(intervals) == 1:
            return [-1]
        for i in range(len(intervals)):
            dict_[tuple(intervals[i])] = i

        inter = sorted(intervals, key = lambda x:x[0])

        for idx1, idx2 in intervals:
            high, low = len(inter) - 1, 0
            index = -1 if (i := bisect_left(inter, [idx2])) >= len(intervals) else dict_[tuple(inter[i])]
            ans.append(index)

        return ans