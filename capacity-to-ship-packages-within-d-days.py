class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (right + left)//2
            sum_ = 0
            count = 0

            for i in range(len(weights)):
                if sum_ + weights[i] <= mid:
                    sum_ += weights[i]
                else:
                    sum_ = weights[i]
                    count +=1

            if count < days:
                right = mid -1
            elif count >= days:
                left = mid + 1
        
        return left