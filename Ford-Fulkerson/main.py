def searching_BFS():
    visit = [False] * n
    visit[source] = True
    queue = [source]

    while queue:
        a = queue.pop(0)
        for b, value in enumerate(G[a]):
            if not visit[b] and value > 0:
                queue.append(b)
                visit[b] = True
                parent[b] = a
    return True if visit[stock] else False


with open('Input.txt', 'r') as Inp:
    G = [list(map(float, line.split())) for line in Inp.read().split('\n')]
    n = len(G)
    source = 0  # int(input())
    stock = 5   # int(input())

parent = [-1] * n
max_flow = 0
while searching_BFS():
    path_flow = float('inf')
    s = stock

    while s != source:
        path_flow = min(path_flow, G[parent[s]][s])
        s = parent[s]
    max_flow += path_flow

    v = stock
    while v != source:
        u = parent[v]
        G[u][v] -= path_flow
        G[v][u] += path_flow
        v = parent[v]

print(f'Максимальный поток: {max_flow}')
