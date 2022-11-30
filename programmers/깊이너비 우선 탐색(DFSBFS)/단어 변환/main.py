from collections import deque
from typing import Deque, List, Tuple


def solution(begin: str, target: str, words: List[str]):
    answer = 0

    length_words = len(begin)

    if target not in words:
        return answer

    # 변환 횟수, 단어
    q_word: Deque[Tuple[int, str]] = deque([(0, begin)])

    while q_word:
        count, word = q_word.popleft()

        if word == target:
            return count

        for word_to_target in words:
            if sum([word[i] != word_to_target[i] for i in range(length_words)]) == 1:
                q_word.append((count + 1, word_to_target))

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)
