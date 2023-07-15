class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums: 
            return 0

        q = set([0])   
        nums = deque(nums)
        running_count = { 0: 1 }

        while nums:
            n = nums.popleft()
            
            next_cnt = dict()
            next_vals = set()

            while(q):   
                val = q.pop()
                l=val+n
                r=val-n
                next_cnt[l] = next_cnt.get(l,0) + running_count[val]
                next_cnt[r] = next_cnt.get(r,0) + running_count[val]
                next_vals.update([l,r])

            running_count = next_cnt
            q=next_vals


        return running_count.get(target,0)