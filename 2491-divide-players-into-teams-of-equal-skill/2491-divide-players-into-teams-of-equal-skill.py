class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        if len(skill) % 2 != 0:
            return -1
        
        skill.sort()
        ptr1 = 0
        ptr2 = len(skill) - 1
        sum_ = skill[ptr1] + skill[ptr2]
        ans = skill[ptr1] * skill[ptr2]
        
        while(ptr1 < ptr2-1):
            ptr1 += 1
            ptr2 -= 1
            
            
            if skill[ptr1] + skill[ptr2] == sum_:
                ans += skill[ptr1] * skill[ptr2]
            else:
                return -1
        
        return ans
        
                
            
            
            
            
        
        