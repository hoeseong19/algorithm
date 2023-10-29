import sys


def solve(a, b, c):
    if b == 1:
        return a % c
    else:
        d = solve(a, b // 2, c)
        if b % 2 == 0:
            return (d * d) % c
        else:
            return (d * d * solve(a, 1, c)) % c


a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(solve(a, b, c))

# with open("./baekjoon/1629/input.txt") as f:
#     for _ in range(int(f.readline().rstrip())):
#         a, b, c = map(int, f.readline().rstrip().split())
#         answer = solve(a, b, c)
#         print(answer == int(f.readline().rstrip()))
