class Solution:
    def solve(self, s: str):
        list_s_sep_by_sub = s.split("-")

        list_sum = []

        for list_s in list_s_sep_by_sub:
            list_sum.append(sum(map(int, list_s.split("+"))))

        answer = list_sum[0]

        if len(list_sum) > 1:
            answer -= sum(list_sum[1:])

        return answer


s = input()
print(Solution().solve(s))


# print(Solution().solve("55-50+40") == -35)

# print(Solution().solve("10+20+30+40") == 100)

# print(Solution().solve("00009-00009") == 0)

# print(Solution().solve("10") == 10)
