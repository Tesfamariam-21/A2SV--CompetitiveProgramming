class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def check_subset(subset):
            diff = [0] * n
            for i, j in subset:
                diff[i] -= 1
                diff[j] += 1
            return all(x == 0 for x in diff)
        
       
        def backtrack(start, subset):
            nonlocal max_requests
            if start == len(requests):
                if check_subset(subset):
                    max_requests = max(max_requests, len(subset))
                return
            backtrack(start+1, subset)
            subset.append(requests[start])
            backtrack(start+1, subset)
            subset.pop()
        
       
        max_requests = 0
        backtrack(0, [])
        return max_requests