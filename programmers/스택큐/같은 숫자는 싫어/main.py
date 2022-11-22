from typing import List

def solution(arr: List[int]):
    answer = []

    for number in arr:
        if len(answer) != 0 and answer[-1] == number:
            answer.pop()

        answer.append(number)
    
    return answer

print(solution([1,1,3,3,0,1,1]) == [1,3,0,1])
print(solution([4,4,4,3,3]) == [4,3])