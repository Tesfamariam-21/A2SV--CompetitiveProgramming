class Solution: 
     def countPairs(self, deliciousness: List[int]) -> int:       
        count = Counter()
        ans = 0
        
        for x in deliciousness:
            for y in range(22):
                target = (1<<y) - x
                
                if target in count:
                    ans += count[target]

            count[x] += 1

        return ans % (10**9 + 7)
                
            
        