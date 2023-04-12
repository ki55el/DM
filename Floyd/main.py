with open('Input.txt', 'r') as Inp:
    D = [[float(j) for j in i.split()] for i in Inp.read().split('\n')]
for d in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            D[i][j] = min(D[i][d] + D[d][j], D[i][j])
[print(*map(int, line)) for line in D]
