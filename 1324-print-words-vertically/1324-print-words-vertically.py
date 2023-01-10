class Solution:
    def printVertically(self, s: str) -> List[str]:
        li = s.split()
        max_ = 0
        l = []
        s = ""
        
        for i in li:
            max_ = max(max_, len(i))
        
        for i in range(max_):
            for j in range(len(li)): 
                try:
                    s += li[j][i]
                except IndexError:
                    s += " "
            s = s.rstrip()
            l.append(s)
            s = ""
 
       
        return l[0:max_]