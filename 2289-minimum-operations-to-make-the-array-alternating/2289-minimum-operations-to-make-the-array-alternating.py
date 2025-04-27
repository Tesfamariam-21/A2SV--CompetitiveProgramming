from collections import Counter

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        odd_count = Counter(nums[i] for i in range(1, n, 2))
        even_count = Counter(nums[i] for i in range(0, n, 2))
        
        odd_most_common = odd_count.most_common(2)
        even_most_common = even_count.most_common(2)
        
        odd_first = odd_most_common[0] if odd_most_common else (0, 0)
        odd_second = odd_most_common[1] if len(odd_most_common) > 1 else (0, 0)
        
        even_first = even_most_common[0] if even_most_common else (0, 0)
        even_second = even_most_common[1] if len(even_most_common) > 1 else (0, 0)
        
        if odd_first[0] == even_first[0]:
            return min(n - odd_first[1] - even_second[1], n - even_first[1] - odd_second[1])
        else:
            return n - odd_first[1] - even_first[1]