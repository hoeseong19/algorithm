from typing import List, Dict, Optional


class Solution:
    # Symbol - Value
    DICT_ROMAN_TO_INT: Dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        list_int: List[int] = []
        sum_int: int = 0

        list_roman = [c for c in s]

        roman_current: str = ''
        roman_before: str = ''

        int_current: Optional[int] = 0
        int_before: Optional[int] = 0

        signed_int_to_be_appended = 0

        while list_roman:
            roman_current = list_roman.pop()
            int_current = self.DICT_ROMAN_TO_INT.get(roman_current)

            int_before = self.DICT_ROMAN_TO_INT.get(roman_before)

            signed_int_to_be_appended = int_current

            if (int_current is not None) and (int_before is not None):
                if int_current < int_before:
                    signed_int_to_be_appended = -int_current

            list_int.append(signed_int_to_be_appended)

            roman_before = roman_current

        sum_int = sum(list_int)

        return sum_int

solution = Solution()

print(solution.romanToInt('III') == 3)
print(solution.romanToInt('LVIII') == 58)
print(solution.romanToInt('MCMXCIV') == 1994)
