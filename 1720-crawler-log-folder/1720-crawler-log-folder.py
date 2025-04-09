class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == "../":
                depth = max(0, depth -1)
            elif log != "./":
                depth +=1

        return depth
        # stack = []

        # for log in logs:
        #     if log == "../":
        #         if stack:
        #             stack.pop()
        #     elif log != "./":
        #         stack.append(log)

        # return len(stack)
            
        