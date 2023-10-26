from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        answer = 0

        arr.sort()

        dict_num_TO_cnt = {}

        for idx, num in enumerate(arr):
            dict_num_TO_cnt[num] = 1

            for child in arr[0:idx]:
                quotient = num // child
                remainder = num % child

                if remainder == 0 and dict_num_TO_cnt.get(quotient) is not None:
                    dict_num_TO_cnt[num] += dict_num_TO_cnt[child] * dict_num_TO_cnt[quotient]

            answer += dict_num_TO_cnt[num]

        return answer % 1_000_000_007


print(Solution().numFactoredBinaryTrees(arr=[6, 3, 2]) == 5)
print(Solution().numFactoredBinaryTrees(arr=[2, 4]) == 3)
print(Solution().numFactoredBinaryTrees(arr=[2, 4, 5, 10]) == 7)
