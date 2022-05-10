from typing import List


def solution(priorities:List[int], location:int):
    answer = 0

    highest_rank = max(priorities)

    # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
    priority_can_be_printted = priorities[0]
    while(not (highest_rank == priority_can_be_printted and location == 0)):
        del priorities[0]
        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if priority_can_be_printted != highest_rank:
            priorities.append(priority_can_be_printted)
        # 3. 그렇지 않으면 J를 인쇄합니다.
        else:
            highest_rank = max(priorities)
            answer += 1

        location -= 1
        if location < 0:
            location = len(priorities) - 1

        priority_can_be_printted = priorities[0]

    answer += 1

    return answer


print(solution([2, 1, 3, 2],2) == 1)
print(solution([1, 1, 9, 1, 1, 1],0) == 5)
