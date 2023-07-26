class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dict_ = Counter(arr)
        
        if len(dict_.values()) == len(set(dict_.values())):
            return True
        
        return False
        