class Solution:
    def solve(self, n: int) -> int:
        answer = 0

        list_count = [None for _ in range(n + 1)]
        list_count[1] = 0

        for i in range(2, n + 1):
            list_prev_index = [i - 1]

            if i % 3 == 0:
                list_prev_index.append(i // 3)
            if i % 2 == 0:
                list_prev_index.append(i // 2)

            list_count[i] = min([list_count[j] for j in list_prev_index]) + 1

        answer = list_count[n]

        return answer


n = int(input())
print(Solution().solve(n))

print(Solution().solve(1000000) == 19)
print(Solution().solve(10) == 3)
print(Solution().solve(5) == 3)
print(Solution().solve(6) == 2)
print(Solution().solve(12) == 3)
print(Solution().solve(81) == 4)
