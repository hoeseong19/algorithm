from typing import List

STATE_LEFT_HAND = 'L'
STATE_RIGHT_HAND = 'R'
DICT_HAND_TO_DEFAULT_STATE = {
    "left": STATE_LEFT_HAND,
    "right": STATE_RIGHT_HAND,
}

GRAPH_DISTANCE_KEYPAD = [
    [0,4,3,4,3,2,3,2,1,2],
    [4,STATE_LEFT_HAND,1,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,3,STATE_RIGHT_HAND],
    [3,1,0,1,2,1,2,3,2,3],
    [4,STATE_LEFT_HAND,1,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,3,STATE_RIGHT_HAND],
    [3,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,1,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND],
    [2,2,1,2,1,0,1,2,1,2],
    [3,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,1,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND],
    [2,STATE_LEFT_HAND,3,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,1,STATE_RIGHT_HAND],
    [1,3,2,3,2,1,2,1,0,1],
    [2,STATE_LEFT_HAND,3,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND,STATE_LEFT_HAND,1,STATE_RIGHT_HAND],
]

DICT_INIT_STATE_TO_LIST_DISTANCE = {
    '*': [1,STATE_LEFT_HAND,4,STATE_RIGHT_HAND,STATE_LEFT_HAND,3,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND],
    '#': [1,STATE_LEFT_HAND,4,STATE_RIGHT_HAND,STATE_LEFT_HAND,3,STATE_RIGHT_HAND,STATE_LEFT_HAND,2,STATE_RIGHT_HAND],
}

def solution(numbers:List[int], hand:str):
    answer = ''

    list_hand_button_pressed = []
    hand_button_pressed = ''

    state_left_hand = '*'
    state_right_hand = '#'

    DEFAULT_STATE = DICT_HAND_TO_DEFAULT_STATE.get(hand)

    for number_idx,number in enumerate(numbers):

        if number in (1, 4, 7):
            state_left_hand = number

            hand_button_pressed = STATE_LEFT_HAND
        elif number in (3, 6, 9):
            state_right_hand = number

            hand_button_pressed = STATE_RIGHT_HAND
        else:
            distance_left_hand_to_the_number = None
            distance_right_hand_to_the_number = None

            if state_left_hand == '*':
                distance_left_hand_to_the_number = DICT_INIT_STATE_TO_LIST_DISTANCE[state_left_hand][number]
            else:
                distance_left_hand_to_the_number = GRAPH_DISTANCE_KEYPAD[state_left_hand][number]

            if state_right_hand == '#':
                distance_right_hand_to_the_number = DICT_INIT_STATE_TO_LIST_DISTANCE[state_right_hand][number]
            else:
                distance_right_hand_to_the_number = GRAPH_DISTANCE_KEYPAD[state_right_hand][number]


            if distance_left_hand_to_the_number > distance_right_hand_to_the_number:
                state_right_hand = number

                hand_button_pressed = STATE_RIGHT_HAND
            elif distance_left_hand_to_the_number < distance_right_hand_to_the_number:
                state_left_hand = number

                hand_button_pressed = STATE_LEFT_HAND
            else:
                if DEFAULT_STATE == STATE_LEFT_HAND:
                    state_left_hand = number

                    hand_button_pressed = STATE_LEFT_HAND
                else: #STATE_RIGHT_HAND
                    state_right_hand = number

                    hand_button_pressed = STATE_RIGHT_HAND

        list_hand_button_pressed.append(hand_button_pressed)

        answer = "".join(list_hand_button_pressed)



    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left") == "LRLLRRLLLRR")
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right") == "LLRLLRLLRL")
