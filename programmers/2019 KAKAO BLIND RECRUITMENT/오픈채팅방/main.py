from typing import Dict, List

INDEX_RECODE_COMMAND = 0
INDEX_RECODE_UID = 1
INDEX_RECODE_NAME = 2

DICT_COMMAND_TO_MESSAGE = {
    "Enter": "님이 들어왔습니다.",
    "Leave": "님이 나갔습니다.",
}

def solution(list_record:List[str]):
    answer = []

    list_tuple_uid_with_message = []

    dict_uid_TO_name:Dict[str,str] = {}

    for record in list_record:
        # 전체 명령어는 띄어쓰기로 구분
        list_splited_record = record.split(' ')

        # 명령어는 첫번째
        command = list_splited_record[INDEX_RECODE_COMMAND]
        # uid는 두번째
        uid = list_splited_record[INDEX_RECODE_UID]

        message = DICT_COMMAND_TO_MESSAGE.get(command)
        # Enter, Leave
        if message is not None:
            list_tuple_uid_with_message.append((uid,message))

            if command == "Enter":
                # 이름은 세번째
                name = list_splited_record[INDEX_RECODE_NAME]

                # 무조건 overwrite
                dict_uid_TO_name[uid] = name

        # Change
        else:
            # 이름은 세번째
            name = list_splited_record[INDEX_RECODE_NAME]

            # 무조건 overwrite
            dict_uid_TO_name[uid] = name

    for tuple_uid_with_message in list_tuple_uid_with_message:
        uid, message = tuple_uid_with_message

        name = dict_uid_TO_name.get(uid)

        total_message = f"{name}{message}"

        answer.append(total_message)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])==["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])
