class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        five = ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 5
            elif bills[i] == 10:
                if five < 5:
                    return False
                five -= 5
                ten += 10

            elif bills[i] == 20:
                if (five > 0 and ten > 0):
                    ten -= 10
                    five -= 5
                    continue
                elif five > 10:
                    five -= 15
                    continue
                
                return False

        return True