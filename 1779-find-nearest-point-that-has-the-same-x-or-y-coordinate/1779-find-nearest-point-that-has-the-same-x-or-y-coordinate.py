class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_ = pow(10, 5)
        index = -1
        
        for i, val in enumerate(points):
            if x == val[0] or y == val[1]:
                manhattan_distance = abs(x - val[0]) + abs(y - val[1])
                if manhattan_distance < min_:
                    min_ = manhattan_distance
                    index =i   
        
        return index