class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0]*k
        minn = float("inf")
        cookies = sorted(cookies, reverse = True)

        def helper(arr, index):
            nonlocal minn
            
            if index >= len(cookies):
                minn = min(minn, max(arr))
                return
    
            if max(arr) >= minn:
                return
            for i in range(0, len(arr)):
                arr[i] += cookies[index]
                helper(arr, index+1)
                arr[i] -= cookies[index]
                 

        helper(arr, 0)
        return minn