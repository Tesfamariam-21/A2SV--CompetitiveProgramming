class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        dict_ = defaultdict(list)

        for i in range(len(rooms)):
            dict_[i].extend(rooms[i])

        q.append(0)

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)

            for num in dict_[node]:
                q.append(num)

        for i in range(len(rooms)):
            if i not in visited:
                return False

        return True