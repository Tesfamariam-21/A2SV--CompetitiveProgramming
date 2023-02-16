n, m = map(int, input().split())
word = []
ans = []

for _ in range(n):
    inp = input()
    word.append(inp)

colWord = [[0 for j in range(n)] for i in range(m)]
words = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        words[i][j] = word[i][j]

for i in range(m):
    for j in range(n):
        colWord[i][j] = words[j][i]


for i in range(n):
    for j in range(m):
        checkRow = words[i][:j] + words[i][j+1:]
        checkCol = colWord[j][:i] + colWord[j][i+1:]

        if word[i][j] in checkRow or word[i][j] in checkCol:
            continue
        else:
            ans.append(word[i][j])

ans = ''.join(ans)
print(ans)
