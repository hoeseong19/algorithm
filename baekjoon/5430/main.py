from typing import List


class Solution:
    def executeArrayOperations(self, operations: str, length_arr: int, arr: List[int]):
        answer = "error"

        s, e = 0, length_arr

        even_r = True

        for o in operations:
            if o == "R":
                even_r = not even_r

            if o == "D":
                if even_r:
                    s += 1
                else:
                    e -= 1

        if s <= e:
            arr = arr[s:e]
            if not even_r:
                arr = arr[::-1]
            answer = f"[{','.join(map(str, arr))}]"

        return answer


number_of_testcases = int(input())
for _ in range(number_of_testcases):
    operations = input()
    length_arr = int(input())
    arr_str = input()

    print(Solution().executeArrayOperations(operations, length_arr, eval(arr_str)))
