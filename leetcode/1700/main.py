from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q_students = deque(students)
        q_sandwiches = deque(sandwiches)

        length_students = len(q_students)

        loop_count = 0

        while q_students:
            # wants to eat the sandwich
            if q_students[0] == q_sandwiches[0]:
                q_students.popleft()
                q_sandwiches.popleft()

                length_students -= 1

                loop_count = 0
            else:
                q_students.append(q_students.popleft())

                loop_count += 1

                if length_students == loop_count:
                    break

        answer = length_students

        return answer


print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0)
print(Solution().countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]) == 3)
