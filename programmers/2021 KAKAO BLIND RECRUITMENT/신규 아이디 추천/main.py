DICT_CHARACTER_TO_IS_NOT_APPROVED = {
    "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"n":0,"m":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,
    "0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,
    "-":0,"_":0,".":0
}
UNAVAILABLE_TEXT_DOUBLE_DOT = '..'
SINGLE_DOT = '.'
CHARACTER_AT_LEAST = 'a'
LENGTH_NEW_ID_LIMIT = 15
MIN_LENGTH_NEW_ID_NOT_ACCEPTED = 16
MIN_LENGTH_NEW_ID_ACCEPTED = 2


def solution(new_id:str):
    answer = ''

    input_new_id = new_id

    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    input_new_id = input_new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    length_new_id = len(input_new_id)
    current_index_in_new_id = 0
    while(length_new_id != current_index_in_new_id):
        char_can_be_removed = input_new_id[current_index_in_new_id]
        if DICT_CHARACTER_TO_IS_NOT_APPROVED.get(char_can_be_removed) is None:
            input_new_id = input_new_id[:current_index_in_new_id] + input_new_id[current_index_in_new_id + 1:]
        else:
            current_index_in_new_id += 1

        length_new_id = len(input_new_id)
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    index_double_dot = input_new_id.find(UNAVAILABLE_TEXT_DOUBLE_DOT)
    while(index_double_dot != -1):
        input_new_id = input_new_id.replace(UNAVAILABLE_TEXT_DOUBLE_DOT, SINGLE_DOT)
        index_double_dot = input_new_id.find(UNAVAILABLE_TEXT_DOUBLE_DOT)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    length_new_id = len(input_new_id)
    last_index_of_new_id = length_new_id-1

    char_first_of_new_id = input_new_id[0]
    char_last_of_new_id = input_new_id[last_index_of_new_id]
    if char_last_of_new_id == SINGLE_DOT:
        input_new_id = input_new_id[:last_index_of_new_id] + input_new_id[last_index_of_new_id + 1:]
    if char_first_of_new_id == SINGLE_DOT:
        input_new_id = input_new_id[:0] + input_new_id[0 + 1:]
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    length_new_id = len(input_new_id)
    if length_new_id == 0:
        input_new_id = CHARACTER_AT_LEAST
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    length_new_id = len(input_new_id)
    if length_new_id > LENGTH_NEW_ID_LIMIT:
        input_new_id = input_new_id[0:LENGTH_NEW_ID_LIMIT]

    length_new_id = len(input_new_id)
    last_index_of_new_id = length_new_id-1

    char_last_of_new_id = input_new_id[last_index_of_new_id]
    if char_last_of_new_id == SINGLE_DOT:
        input_new_id = input_new_id[:last_index_of_new_id] + input_new_id[last_index_of_new_id + 1:]
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    length_new_id = len(input_new_id)
    while (length_new_id <= MIN_LENGTH_NEW_ID_ACCEPTED):
        last_index_of_new_id = length_new_id-1
        char_last_of_new_id = input_new_id[last_index_of_new_id]

        input_new_id = ''.join((input_new_id,char_last_of_new_id))

        length_new_id = len(input_new_id)

    answer = input_new_id

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
print(solution("z-+.^.") == "z--")
print(solution("=.=") == "aaa")
print(solution("123_.def") == "123_.def")
print(solution("abcdefghijklmn.p") == "abcdefghijklmn")
