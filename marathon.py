t = int(input())

for i in range(t):
    in_front = 0
    a, b, c, d = list(map(int, input().split()))

    if b > a:
        in_front += 1
    if c > a:
        in_front += 1
    if d > a:
        in_front += 1

    print(in_front)