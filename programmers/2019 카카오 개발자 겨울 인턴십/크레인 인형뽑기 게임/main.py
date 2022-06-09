from typing import List

import numpy as np

# 인형이 없음
INDEX_DOLL_TYPE_NOTHING = 0



# 만약 효율성 실패 시에
# column 별로 해시 만들어서, 각각 뽑아야될 인덱스를 저장

def solution(list2_board:List[List[int]], list_move:List[int]):
    answer = 0

    # length 를 구하는 if를 사용하지 않기 위해, 0을 미리 삽입
    list_moved = [INDEX_DOLL_TYPE_NOTHING]

    list2_transposed_board = np.array(list2_board).T.tolist()

    for move in list_move:
        index_move = move - 1

        list_board = list2_transposed_board[index_move]

        for index_board, index_doll_type in enumerate(list_board):
            if index_doll_type == INDEX_DOLL_TYPE_NOTHING:
                continue
            else:
                list_moved.append(index_doll_type)

                list_board[index_board] = INDEX_DOLL_TYPE_NOTHING


                index_lastest_doll_type = list_moved[-1]
                index_prev_lastest_doll_type = list_moved[-2]
                if index_lastest_doll_type == index_prev_lastest_doll_type:
                    list_moved.pop()
                    list_moved.pop()

                    answer += 2

                break

    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]) == 4)
