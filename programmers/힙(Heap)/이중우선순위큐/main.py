from heapq import heapify, heappop, heappush
from typing import List

COMMAND_INSERT = 'I'
COMMAND_DELETE = 'D'


def solution(operations: List[str]):
    answer = []

    heapify(answer)

    for operation in operations:
        operation, number = operation.split(' ')
        number = int(number)

        if operation == COMMAND_INSERT:
            heappush(answer, number)
        else:
            if len(answer) == 0:
                continue
            else:
                if number >= 0:
                    answer.pop()
                    heapify(answer)
                else:
                    heappop(answer)

    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]


print(solution(["I 16", "I -5643", "D -1",
      "D 1", "D 1", "I 123", "D -1"]) == [0, 0])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45",
      "I 97", "D 1", "D -1", "I 333"]) == [333, -45])
