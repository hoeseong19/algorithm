# Lv.2 월간 코드 챌린지 시즌2>음양 더하기

from typing import List

INDEX_LIST_ORIGINAL_NEGATIVE = 0
INDEX_LIST_ORIGINAL_POSITIVE = 1

def solution(list_absolute:List[int], list_bool_sign:List[bool]):
    answer = 123456789

    list_int_sign = list(map(int, list_bool_sign))

    list_positive = []
    list_negative = []
    list2_original = [list_negative, list_positive]

    for absolute in list_absolute:
        list2_original[INDEX_LIST_ORIGINAL_POSITIVE].append(absolute)
        list2_original[INDEX_LIST_ORIGINAL_NEGATIVE].append(-absolute)

    sum_original = 0

    for index_int_sign, int_sign in enumerate(list_int_sign):
        number_original = list2_original[int_sign][index_int_sign]

        sum_original += number_original

    answer = sum_original

    return answer

print(solution([4, 7, 12], [True, False, True]) == 9)
print(solution([1, 2, 3], [False, False, True]) == 0)
