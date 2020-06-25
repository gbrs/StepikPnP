n = int(input())
m = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1

for k in range(n * n):
    m[i][j] = k + 1
    if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
        di, dj = dj, -di
    i, j = i + di, j + dj

[print(*i) for i in m]
