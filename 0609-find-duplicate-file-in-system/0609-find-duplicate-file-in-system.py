class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        li = []
        dict_ = {}

        for i in range(len(paths)):
            
            dirs = paths[i].split(" ")
            
            for j in range(1,len(dirs)):
                contentFirstIndex = dirs[j].index("(")
                contentLastIndex = dirs[j].index(")")
                content = dirs[j][contentFirstIndex + 1: contentLastIndex]
                file = dirs[j][0:contentFirstIndex]
                if content in dict_:
                    dict_[content].append(dirs[0] + "/" + file )
                else:
                    dict_[content] = [dirs[0] + "/" +  file]

        for directorys in dict_.values():
            if len(directorys) == 1:
                continue
            else:
                li.append(directorys)
        
        return li
                
                
            
        