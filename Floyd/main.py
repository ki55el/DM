with open('Input.txt', 'r') as Inp:
    D = [[float(j) for j in i.split()] for i in Inp.read().split('\n')]
for k in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            D[i][j] = min(D[i][k] + D[k][j], D[i][j])
[print(*line) for line in D]
