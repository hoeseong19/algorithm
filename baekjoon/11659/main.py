# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())

# sum = 0
# list_prefix_sum = [0]
# for num in sys.stdin.readline().rstrip().split():
#     sum += int(num)
#     list_prefix_sum.append(sum)

# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().rstrip().split())

#     print(list_prefix_sum[j] - list_prefix_sum[i - 1])

with open("baekjoon/11659/input.txt") as f:
    n, m = map(int, f.readline().rstrip().split())

    sum = 0
    list_prefix_sum = [0]
    for num in f.readline().rstrip().split():
        sum += int(num)
        list_prefix_sum.append(sum)

    for _ in range(m):
        i, j = map(int, f.readline().rstrip().split())

        print(list_prefix_sum[j] - list_prefix_sum[i - 1])
