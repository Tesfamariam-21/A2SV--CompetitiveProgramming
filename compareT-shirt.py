def calculateGreater(shirt):
    size = len(shirt)
    sum_ = 0

    dict_ = {
        "S" : -1,
        "M" : 0,
        "L" : 1,
            }
    sum_ = size * dict_[shirt[-1]]

    return sum_
  

inp = int(input())

for i in range(inp):
    t1, t2 = map(calculateGreater, input().split())
    if t1 == t2:
        print("=")
    elif t1 > t2:
        print(">")
    else:
        print("<")
