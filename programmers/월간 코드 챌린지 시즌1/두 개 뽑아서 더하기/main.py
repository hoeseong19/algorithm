def solution(numbers):
    answer = []

    MAX_NUMBER = max(numbers)
    MAX_COUNT = len(numbers)

    array_number = [0 for _ in range(MAX_NUMBER * MAX_COUNT + 1)]

    for index_number, number in enumerate(numbers):
        for number_another in numbers[index_number+1:]:
            sum = number + number_another

            array_number[sum] += 1

    for index_number, count_number in enumerate(array_number):
        if count_number > 0:
            answer.append(index_number)

    return answer

print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])