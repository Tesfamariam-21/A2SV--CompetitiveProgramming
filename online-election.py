class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.answer = []
        self.counter = defaultdict(int)
        self.Max = self.persons[0]
        self.MaxCount = 1

        for person in self.persons:
            self.counter[person] += 1
            if self.counter[person] >= self.MaxCount:
                self.answer.append(person)
                self.Max = person
                self.MaxCount = self.counter[person]
            else:
                self.answer.append(self.Max)
       
    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)
        return self.answer[index-1]
       


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)