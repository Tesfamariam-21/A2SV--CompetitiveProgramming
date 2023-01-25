class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        left = 0
        right = len(people) - 1
        people.sort()
        
        
        for i in range(len(people)):
            if people[i] > limit:
                right = i
                break
        
        while(left <= right):
            if people[right] == limit:
                boat += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                boat += 1
                right -= 1
                left += 1
            elif people[left] + people[right] > limit:
                boat += 1
                right -= 1
   
        return boat
        
        