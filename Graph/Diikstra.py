def diikstra(G, a, z):
    n = len(G)
    L = [float("infinity")] * n 
    L[a] = 0
    S = [False] * n 
    while not S[z]:
        min_L = float("infinity")
        min_index = None 
        for i in range(n):
            if not S[i] and L[i] < min_L:
                min_L = L[i]
                min_index = i
        u = min_index 
        S[u] = True 
        for v in range(n):
            if not S[v] and G[u][v] != 0 and L[u] + G[u][v] < L[v]:
                L[v] = L[u] + G[u][v]
    return L[z]

G = [
    [0, 5, 2, 0, 0, 0],
    [5, 0, 1, 4, 0, 0],
    [2, 1, 0, 7, 9, 0],
    [0, 4, 7, 0, 3, 6],
    [0, 0, 9, 3, 0, 2],
    [0, 0, 0, 6, 2, 0],
]

print(diikstra(G, 0, 5))

