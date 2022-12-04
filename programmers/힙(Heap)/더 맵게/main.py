from heapq import heapify, heappop, heappush


def solution(scoville, K):
    answer = 0

    length_scoville = len(scoville)

    heapify(scoville)

    while length_scoville >= 2:
        scoville_first = heappop(scoville)
        if scoville_first >= K:
            break
        else:
            scoville_second = heappop(scoville)

            heappush(scoville, scoville_first + scoville_second * 2)

            answer += 1

            length_scoville = len(scoville)

    if length_scoville == 0:
        answer = -1
    if length_scoville == 1:
        if heappop(scoville) < K:
            answer = -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
print(solution([1], 7) == -1)
print(solution([1, 9], 7) == 1)
print(solution([1, 2], 7) == -1)
print(solution([], 7) == -1)
