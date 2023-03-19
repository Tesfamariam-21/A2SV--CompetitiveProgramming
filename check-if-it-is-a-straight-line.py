class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True

        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

        for x3, y3 in coordinates:
            if (x2 - x1) *(y3 - y1) != (x3 - x1) * (y2 - y1):
                return False

        return True