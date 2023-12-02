from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0

        counter_chars = Counter(chars)

        for word in words:
            counter_word = Counter(word)

            is_able_to_be_formed = all([counter_chars[c] >= counter_word[c] for c in word])

            if is_able_to_be_formed:
                answer += len(word)

        return answer


print(Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6)
print(Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10)
