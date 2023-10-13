from typing import List


class Solution:
    def solve(self, n: int, list_waiting_time: List[int]):
        answer = 0

        list_waiting_time.sort()

        for i in range(0, n):
            answer += (n - i) * list_waiting_time[i]

        return answer


n = int(input())
list_waiting_time = [i for i in map(int, input().split(" "))]
print(Solution().solve(n, list_waiting_time))
