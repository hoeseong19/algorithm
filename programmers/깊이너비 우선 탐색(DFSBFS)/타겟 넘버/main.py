def solution(numbers, target):
    answer = 0

    length_numbers = len(numbers)

    def dfs(sum, index):
        if index >= length_numbers:
            if sum == target:
                return 1
            else:
                return 0
        else:
            return dfs(sum + numbers[index], index + 1) + dfs(sum - numbers[index], index + 1)

    answer = dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3) == 5)
print(solution([4, 1, 2, 1], 4) == 2)
