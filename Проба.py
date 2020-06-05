arr = []
arr.append(list(input().split()))
N = len(arr[0])

for i in range(1, N):
    line = list(input().split())
    arr.append(line)
print(arr)

# границы уже обойденного поля
left = up = 0
right = down = N - 1

while True:
    if left > right:
        break
    for column in range(left, right + 1):
        print(arr[up][column], end=' ')
    print()
    up += 1

    if up > down:
        break
    for line in range(up, down + 1):
        print(arr[line][right], end=' ')
    print()
    right -= 1

    if left > right:
        break
    for column in range(right, left - 1, -1):
        print(arr[down][column], end=' ')
    print()
    down -= 1

    if up > down:
        break
    for line in range(down, up - 1, -1):
        print(arr[line][left], end=' ')
    print()
    left += 1

# for i in range(len(arr)):
#     for j in range(len(arr[0])):
