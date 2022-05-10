DICT_NUMBER_STRING_TO_NUMBER = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

def solution(s:str):
    answer = 0
    list_number = []

    index_flag = 0

    for idx, c in enumerate(s):
        index_will_be_next_flag = idx+1

        if c.isnumeric():
            list_number.append(c)
            index_flag = index_will_be_next_flag
            continue

        string_can_be_number = s[index_flag:index_will_be_next_flag]
        number = DICT_NUMBER_STRING_TO_NUMBER.get(string_can_be_number)

        if number is None:
            continue

        list_number.append(number)
        index_flag = index_will_be_next_flag

    answer = int(''.join(list_number))

    return answer

print(solution("one4seveneight") == 1478)
print(solution("23four5six7") == 234567)
print(solution("2three45sixseven") == 234567)
print(solution("123") == 123)
