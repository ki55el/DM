with open('Input.txt', 'r') as Inp:
    C = [[float(j) for j in i.split()] for i in Inp.read().split('\n')]
n = len(C)
d = [[float('inf') for _ in range(n)] for _ in range(n)]
x = 0   # int(input())
for k in range(n):
    for i in range(n):
        d[k][x] = 0
        d[k][i] = min([d[k-1][j] + C[j][i] for j in range(n)])
[print(*_) for _ in d]
