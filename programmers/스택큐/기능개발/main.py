from collections import deque


def solution(progresses, speeds):
    answer = []

    q_progress = deque(progresses)
    q_speed = deque(speeds)

    count = 0

    while q_progress:
        if q_progress[0] >= 100:
            q_progress.popleft()
            q_speed.popleft()

            count += 1
        else:
            answer.append(count)
            count = 0
            for index_progress in range(len(q_progress)):
                q_progress[index_progress] += q_speed[index_progress]

    answer.append(count)

    return [i for i in answer if i != 0]


print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])
