class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ""

        for i in range(len(num) - 2):
            if len(set(num[i : i + 3])) == 1:
                answer = max(answer, num[i : i + 3])

        return answer


print(Solution().largestGoodInteger(num="6777133339") == "777")
print(Solution().largestGoodInteger(num="2300019") == "000")
print(Solution().largestGoodInteger(num="42352338") == "")
