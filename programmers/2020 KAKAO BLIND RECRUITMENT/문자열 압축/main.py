from typing import Dict, List

def get_length_list_compressed_pattren_string(list_pattren_string:List[str]):
    list_compressed_pattren_string = []

    counter = 0
    prev_pattren_string = None
    for pattren_string in list_pattren_string:
        if prev_pattren_string is None:
            prev_pattren_string = pattren_string
            counter += 1
        else:
            if prev_pattren_string == pattren_string:
                counter += 1
            else:
                if counter != 1:
                    list_compressed_pattren_string.append(str(counter))
                list_compressed_pattren_string.append(prev_pattren_string)

                prev_pattren_string = pattren_string

                counter = 1
    if counter != 1:
        list_compressed_pattren_string.append(str(counter))
    list_compressed_pattren_string.append(prev_pattren_string)

    string_compressed_by_pattern = "".join(list_compressed_pattren_string)
    length_string_compressed_by_pattern = len(string_compressed_by_pattern)

    return length_string_compressed_by_pattern


def solution(string_can_be_compressed:str):
    answer = 0

    length_string_can_be_compressed = len(string_can_be_compressed)
    minimum_length_string_can_be_compressed = length_string_can_be_compressed

    # 자기 자신을 제외한 공약수를 dict로 관리
    dict_divisor_TO_list_pattren_string:Dict[int,List[str]] = {}
    for i in range(1,length_string_can_be_compressed):
        dict_divisor_TO_list_pattren_string[i] = []

    for divisor,list_pattren_string in dict_divisor_TO_list_pattren_string.items():
        # 공약수가 step이 돼서 step 만큼 slicing
        index_slicing = 0
        while (index_slicing < length_string_can_be_compressed):
            min_ = min(index_slicing+divisor,length_string_can_be_compressed)
            pattren_string = string_can_be_compressed[index_slicing:min_]
            list_pattren_string.append(pattren_string)

            index_slicing+=divisor

        # 압축
        length_list_compressed_pattren_string = get_length_list_compressed_pattren_string(list_pattren_string)
        if minimum_length_string_can_be_compressed > length_list_compressed_pattren_string:
            minimum_length_string_can_be_compressed = length_list_compressed_pattren_string

    answer = minimum_length_string_can_be_compressed

    return answer

print(solution("aabbaccc")==7)
print(solution("ababcdcdababcdcd")==9)
print(solution("abcabcdede")==8)
print(solution("abcabcabcabcdededededede")==14)
print(solution("xababcdcdababcdcd")==17)
