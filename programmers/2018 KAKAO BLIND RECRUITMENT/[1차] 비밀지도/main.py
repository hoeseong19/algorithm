def changeNumberSystem(number, n=2):

    quotient = number // n
    remainder = number % n

    if quotient < n:
        return str(quotient) + str(remainder)
    else:
        return changeNumberSystem(quotient) + str(remainder)

INTEGER_BLANK = "0"
INTEGER_WALL = "1"
STRING_BLANK = " "
STRING_WALL = "#"

DICT_TUPLE_CELL_TO_OVERLAPPED_CELL = {
    (INTEGER_BLANK, INTEGER_BLANK): STRING_BLANK,
    (INTEGER_BLANK, INTEGER_WALL): STRING_WALL,
    (INTEGER_WALL, INTEGER_BLANK): STRING_WALL,
    (INTEGER_WALL, INTEGER_WALL): STRING_WALL,
}

def overlapCell(cell1, cell2):
    overlapped_cell = DICT_TUPLE_CELL_TO_OVERLAPPED_CELL.get((cell1, cell2))

    return overlapped_cell

# 차원 변경
def parseMap(n, arr):
    LENGTH_ARRAY = n

    map = [[STRING_BLANK for _ in range(LENGTH_ARRAY)] for _ in range(LENGTH_ARRAY)]

    for i in range(LENGTH_ARRAY):
        binary = changeNumberSystem(arr[i], 2)

        binary = binary.zfill(LENGTH_ARRAY)

        for j in range(LENGTH_ARRAY):
            map[i][j] = binary[j]

    return map

# 지도 겹치기
def decodeMap(n, arr1, arr2):

    LENGTH_ARRAY = n

    secret_map = [[STRING_BLANK for _ in range(LENGTH_ARRAY)] for _ in range(LENGTH_ARRAY)]

    for i in range(LENGTH_ARRAY):
        for j in range(LENGTH_ARRAY):
            cell1 = arr1[i][j]
            cell2 = arr2[i][j]

            overlapped_cell = overlapCell(cell1, cell2)

            secret_map[i][j] = overlapped_cell

    return secret_map

def solution(n, arr1, arr2):
    answer = []

    map1 = parseMap(n,arr1)
    map2 = parseMap(n,arr2)

    arr2_decoded_map = decodeMap(n, map1, map2)

    for arr_decoded_map in arr2_decoded_map:
        answer.append("".join(arr_decoded_map))

    return answer

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
solution(6,[46, 33, 33, 22, 31, 50],[27, 56, 19, 14, 14, 10])
