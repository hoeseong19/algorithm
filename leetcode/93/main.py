from typing import List, Optional
from copy import deepcopy


class Solution:
    ARRAY_MAX_LENGTH = [12, 9, 6, 3]
    ARRAY_MIN_LENGTH = [4, 3, 2, 1]

    MAX_IP = 255
    MIN_IP = 0

    MAX_LENGTH = 3

    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def divideString(s: str, order: int, prev_s: List[str]):
            length_string = len(s)

            if length_string > self.ARRAY_MAX_LENGTH[order]\
                    or length_string < self.ARRAY_MIN_LENGTH[order]:
                return
            else:
                for i in range(1, min(length_string, self.MAX_LENGTH) + 1):
                    cur_s = s[:i]
                    cur_int = int(cur_s)

                    # cannot have leading zeros.
                    if (cur_s == str(cur_int)) and ((cur_int >= self.MIN_IP) and (cur_int <= self.MAX_IP)):

                        if (order == 3):
                            if (len(s[i:]) == 0):
                                answer.append('.'.join([*prev_s, cur_s]))
                        else:
                            divideString(s[i:], order+1,
                                         deepcopy([*prev_s, cur_s]))

        divideString(s, 0, [])

        return answer


print(Solution().restoreIpAddresses(s="25525511135")
      == set(["255.255.11.135", "255.255.111.35"]))
print(Solution().restoreIpAddresses(s="0000") == set(["0.0.0.0"]))
print(Solution().restoreIpAddresses(s="101023") == set(
    ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]))
