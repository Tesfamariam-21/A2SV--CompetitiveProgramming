class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict_ = {}
        res = []

        for i in range(len(words[0])):
            if words[0][i] in dict_:
                dict_[words[0][i]] = dict_[words[0][i]] + 1
            else:
                dict_[words[0][i]] = 1
        
        for i in range(1, len(words)):
            dict2_ = Counter(words[i])

            for key in dict_:
                if key in dict2_:
                    dict_[key] = min(dict_[key], dict2_[key])
                else:
                    dict_[key] = 0

        for key, count in dict_.items():
            for _ in range(count):
                res.append(key)
        # res = [key for key, count in dict_.items() for _ in range(count)]
        return res



# class Solution:
#     from collections import Counter
#     def commonChars(self, words: List[str]) -> List[str]:
#         ans = []
#         word = Counter(words[0])
        
        
#         for i in range(1, len(words)):
#             c = Counter(words[i])
            
#             for j in word:
#                 word[j] = min(word[j], c[j])
                    
#         print(word)
#         print(list(word.elements()))
#         return list(word.elements())
        
        


