class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        leftPointer = 0
        rightPointer = leftPointer + 1
        count = 0

        while rightPointer < len(words):
            slow = words[leftPointer]
            fast = words[rightPointer]
            min_ = min(len(slow), len(fast))
            print(slow, fast)
            
            if len(slow) > len(fast) and fast == slow[0:min_]:
                return False
            # elif len(slow) < len(fast) and slow == fast[0:min_]:
            #     return False
            
            for i in range(min_):
                count +=1
                print(count)
                if slow[i] == fast[i]:
                    continue
                else:
                    if order.index(slow[i]) < order.index(fast[i]):
                        if len(words) == 2:
                            return True
                        continue
                    elif order.index(slow[i]) > order.index(fast[i]):
                        return False
             
            leftPointer +=1
            rightPointer +=1
                    
        return True
                        
                        