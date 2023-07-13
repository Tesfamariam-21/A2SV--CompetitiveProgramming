class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        dict_ = defaultdict(list)
        prereq = [0 for _ in range(numCourses)]
        

        for course, pre in prerequisites:
            dict_[pre].append(course)
            prereq[course] +=1

        for i in range(numCourses):
            if prereq[i] == 0:
                q.append(i)

        while q:
            length = len(q)

            for i in range(length):
                ele = q.popleft()

                for p in dict_[ele]:
                    prereq[p] -= 1
                    if prereq[p] == 0:
                        q.append(p)


        for i in prereq:
            if i != 0:
                return False

        return True