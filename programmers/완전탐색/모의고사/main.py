# Lv.1 완전탐색>모의고사

COUNT_MATH_GIVER = 3

LIST_PATTERN_MATH_GIVER1 = [1, 2, 3, 4, 5]
LIST_PATTERN_MATH_GIVER2 = [2, 1, 2, 3, 2, 4, 2, 5]
LIST_PATTERN_MATH_GIVER3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

class MathGiver():

    def __init__(self, list_pattern):
        self.list_pattern = list_pattern
        self.length_list_pattern = len(list_pattern)

        self.count_correct = 0

    def solve(self,index_answer_of_exam,answer_of_exam):
        index_answer_mine = index_answer_of_exam % self.length_list_pattern
        answer_mine = self.list_pattern[index_answer_mine]

        if answer_of_exam == answer_mine:
            self.count_correct += 1

        return

def solution(answers):
    answer = []

    math_giver1 = MathGiver(LIST_PATTERN_MATH_GIVER1)
    math_giver2 = MathGiver(LIST_PATTERN_MATH_GIVER2)
    math_giver3 = MathGiver(LIST_PATTERN_MATH_GIVER3)

    list_math_giver = [math_giver1, math_giver2, math_giver3]

    for index_answer_of_exam, answer_of_exam in enumerate(answers):
        for index_math_giver in range(COUNT_MATH_GIVER):
            list_math_giver[index_math_giver].solve(index_answer_of_exam, answer_of_exam)

    max_count_correct = max([math_giver.count_correct for math_giver in list_math_giver])

    for index_math_giver in range(COUNT_MATH_GIVER):
        math_giver = list_math_giver[index_math_giver]
        count_correct = math_giver.count_correct

        if max_count_correct == count_correct:
            answer.append(index_math_giver+1)


    return answer

print(solution([1, 2, 3, 4, 5]) == [1])
print(solution([1, 3, 2, 4, 2]) == [1, 2, 3])
