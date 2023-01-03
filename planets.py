testCase = int(input())

for i in range(testCase):
    dict_ = {}
    sum_ = 0
    planetNum, cost = map(int, input().split())
    orbits = list(map(int, input().split()))
    for orb in orbits:
        if orb in dict_:
            dict_[orb] += 1
        else:
            dict_[orb] = 1

    if cost == 1:
        print(len(dict_))
    else:
        for orb in dict_.values():
            if orb > cost:
                sum_ += cost
            elif orb == cost:
                sum_ += orb
            else:
                sum_ += orb

        print(sum_)

