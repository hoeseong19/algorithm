# Lv.1 Summer/Winter Coding(~2018)>소수 만들기

import math
from itertools import combinations


# https://geekflare.com/prime-number-in-python/
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

R_COMBINATION = 3

def solution(nums):
    answer = 0

    list_tuple_num = combinations(nums, R_COMBINATION)

    for tuple_num in list_tuple_num:
        sum_tuple_num = sum(tuple_num)

        if is_prime(sum_tuple_num):
            answer += 1

    return answer
