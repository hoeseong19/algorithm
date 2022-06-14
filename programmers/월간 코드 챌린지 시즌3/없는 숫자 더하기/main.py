def solution(numbers):
    # 반대로 생각하자
    # 0-9의 모든 수를 더해서, sum(numbers) 만큼 빼자

    answer = -1

    LIST_ZERO_TO_NINE = [i for i in range(10)]
    SUM_ZERO_TO_NINE = sum(LIST_ZERO_TO_NINE)

    sum_numbers = sum(numbers)

    answer = SUM_ZERO_TO_NINE - sum_numbers

    return answer

print(solution([1, 2, 3, 4, 6, 7, 8, 0]) == 14)
print(solution([5, 8, 4, 0, 6, 7, 9]) == 6)
