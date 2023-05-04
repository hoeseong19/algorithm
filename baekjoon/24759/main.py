from typing import List

# n, c = [int(number) for number in input().split(' ')]
# list_w = [int(number) for number in input().split(' ')]


def solution(n: int, c: int, list_w: List[int]):
    list_answer = []
    list_count_start = []
    list_prefix_sum = [0]

    prefix_sum = 0
    for w in list_w:
        list_answer.append(0)
        list_count_start.append(0)

        prefix_sum += w
        list_prefix_sum.append(prefix_sum)

    s, e = 1, 1

    count = 1

    list_count_start[s-1] = count

    while (s <= n):

        count += 1

        if ((e + 1) > n):
            list_answer[s-1] = count - list_count_start[s-1]
            s += 1

        elif ((list_prefix_sum[e+1] - list_prefix_sum[s-1]) > c):
            list_answer[s-1] = count - list_count_start[s-1]
            s += 1

        else:
            e += 1
            list_count_start[e-1] = count

    [print(answer) for answer in list_answer]


solution(5, 3, [1, 1, 1, 2, 2])
print()
solution(5, 10, [1, 2, 3, 4, 5])
