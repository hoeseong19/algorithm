from collections import deque

INDEX_AVAILABLE = 1
INDEX_UNAVAILABLE = 0


def solution(maps):
    answer = -1

    length_row = len(maps)
    length_col = len(maps[0])

    # (지나간 칸의 개수, 시작 위치)로 queue 초기화
    # queue 이므로 depue로 왼쪽 pop 시간 복잡도 줄이기
    q_route = deque([[1, 0, 0]])

    while q_route:
        count, index_row, index_col = q_route.popleft()

        # 지도를 벗어나면 안됨
        if ((index_row < 0) or (index_col < 0)) or ((index_row >= length_row) or (index_col >= length_col)):
            continue

        # 벽이면 지나갈 수 없음
        if maps[index_row][index_col] == INDEX_UNAVAILABLE:
            continue

        # 상대편 진영 도착 여부
        if (index_row == (length_row - 1)) and (index_col == (length_col - 1)):
            return count

        # 지나간 경로 표시
        maps[index_row][index_col] = INDEX_UNAVAILABLE

        # 주변 탐색
        q_route.append([count + 1, index_row, index_col + 1])
        q_route.append([count + 1, index_row, index_col - 1])
        q_route.append([count + 1, index_row + 1, index_col])
        q_route.append([count + 1, index_row - 1, index_col])

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11)
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1)
