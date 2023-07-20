from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []

        while asteroids:
            asteroid = asteroids.pop()

            # 추가되는 소행성이 + 일 경우에만 충돌의 가능성이 있음
            if asteroid > 0:
                answer.append(asteroid)

                length_answer = len(answer)
                index_asteroid = length_answer - 1

                if length_answer != 1:
                    index_prev_asteroid = index_asteroid - 1

                    # 이전에 추가된 소행성이 - 일 경우에만 가능성 검토
                    while index_asteroid != 0 and answer[index_prev_asteroid] < 0:
                        result_collision = answer[index_asteroid] + \
                            answer[index_prev_asteroid]
                        if result_collision > 0:
                            answer = answer[:index_prev_asteroid] + \
                                answer[index_asteroid:]

                            index_prev_asteroid -= 1
                            index_asteroid -= 1
                        # 둘 다 파괴됨
                        elif result_collision == 0:
                            answer.pop()
                            answer.pop()
                            break
                        else:
                            answer.pop()
                            break

            else:
                answer.append(asteroid)

        return answer[::-1]


print(Solution().asteroidCollision(asteroids=[5, 10, -5]) == [5, 10])
print(Solution().asteroidCollision(asteroids=[8, -8]) == [])
print(Solution().asteroidCollision(asteroids=[10, 2, -5]) == [10])
print(Solution().asteroidCollision(asteroids=[-2, 2, -1, -2]) == [-2])
