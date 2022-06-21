
INDEX_WIDTH = 0
INDEX_HEIGHT = 1
COUNT_LIST_SIZE = 2

def sortList2Size(list2_size):
    for list_size in list2_size:
        width_before = list_size[INDEX_WIDTH]
        height_before = list_size[INDEX_HEIGHT]

        width = max(width_before, height_before)
        height = min(width_before, height_before)

        list_size[INDEX_WIDTH] = width
        list_size[INDEX_HEIGHT] = height

    return

def transposeList2Size(list2_size):
    count_row = len(list2_size)

    array2_size = [[0 for _ in range(count_row)] for _ in range(COUNT_LIST_SIZE)]

    for index_list_size, list_size in enumerate(list2_size):
        width = list_size[INDEX_WIDTH]
        height = list_size[INDEX_HEIGHT]

        array2_size[INDEX_WIDTH][index_list_size] = width
        array2_size[INDEX_HEIGHT][index_list_size] = height

    return array2_size


def solution(sizes):
    answer = 0

    sortList2Size(sizes)

    array2_size = transposeList2Size(sizes)

    max_width = max(array2_size[INDEX_WIDTH])
    max_height = max(array2_size[INDEX_HEIGHT])

    answer = max_width * max_height

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133)
