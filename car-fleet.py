class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position = list(zip(position, speed))
        position = sorted(position)

        for i in range(len(position) - 1, -1, -1):
            time = (target - position[i][0])/position[i][1]
            
            if stack and stack[-1] >= time:
                continue             
            stack.append(time)

        return len(stack)