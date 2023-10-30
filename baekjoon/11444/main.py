import sys

sys.setrecursionlimit(10**6)

dict_num_to_result = {}


def solve(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    if dict_num_to_result.get(n) is None:
        if n % 2 == 0:
            a = solve(n // 2 + 1) % 1_000_000_007
            b = solve(n // 2 - 1) % 1_000_000_007
            dict_num_to_result[n] = (a**2 - b**2) % 1_000_000_007
        else:
            a = solve((n + 1) // 2) % 1_000_000_007
            b = solve((n + 1) // 2 - 1) % 1_000_000_007
            dict_num_to_result[n] = (a**2 + b**2) % 1_000_000_007

    return dict_num_to_result[n]


n = int(sys.stdin.readline().rstrip())
print(solve(n))

with open("./baekjoon/11444/input.txt", "r") as f:
    n = int(f.readline().rstrip())
    print(solve(n) == int(f.readline().rstrip()))
