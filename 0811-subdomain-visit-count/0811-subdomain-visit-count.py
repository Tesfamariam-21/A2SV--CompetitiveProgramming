class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        dict_ = defaultdict(int)
        li = []

        for i in range(len(cpdomains)):
            split = cpdomains[i].split()
            dict_[split[1]] += int(split[0])
            
            while split[1].count(".") != 0:
                rep = 0
                index = split[1].index(".") + 1
                split[1] = split[1][index:len(split[1])]
                
                for j in dict_:
                    if j == split[1]:
                        rep += dict_[j]
                dict_[split[1]] = rep + int(split[0])
        
        return ["%d %s"% (dict_[key], key) for key in dict_]

                
#         counter = Counter()
#         li = []
        
#         for i in range(len(cpdomains)):
#             rep, d = cpdomains[i].split()
#             counter[d] += int(rep)
            
#             while d.count(".") != 0:
#                 index = d.index(".") + 1
#                 d = d[index:len(d)]
#                 counter[d] += int(rep)
                
#         for key in counter:
#             li.append(str(counter[key]) + " " + key)
        
#         return li
                
                
                
                
                
                