from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_fizz_buzz: List[str] = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                list_fizz_buzz.append("FizzBuzz")
            elif i % 3 == 0:
                list_fizz_buzz.append("Fizz")
            elif i % 5 == 0:
                list_fizz_buzz.append("Buzz")
            else:
                list_fizz_buzz.append(str(i))

        return list_fizz_buzz


solution = Solution()

print(solution.fizzBuzz(3) == ["1", "2", "Fizz"])
print(solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"])
print(solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz",
      "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
