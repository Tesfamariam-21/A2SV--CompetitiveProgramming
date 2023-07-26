class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def can_arrive_on_time(dist, hour, speed):
            total_time = 0
            for d in dist[:-1]:
                total_time += math.ceil(d / speed)
            total_time += dist[-1] / speed
            return total_time <= hour
        
        left, right = 1, 10**7
        while left < right:
            mid = (left + right) // 2
            if can_arrive_on_time(dist, hour, mid):
                right = mid
            else:
                left = mid + 1
        return left if can_arrive_on_time(dist, hour, left) else -1