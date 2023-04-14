with open('Input.txt', 'r') as Inp:
    G = [[float(j) for j in i.split()] for i in Inp.read().split('\n')]
V = list(range(len(G)))
v = V.pop(0)   # int(input())
S = 0
for i in range(len(G)-1):
    d, v = min([(G[v][j], j) for j in V])
    S += d
    V.remove(v)
print(S)
