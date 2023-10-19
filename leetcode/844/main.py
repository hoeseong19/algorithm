class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        answer = False

        def getFinal(s: str):
            stack = []

            for c in s:
                if c == "#":
                    if len(stack) != 0:
                        stack.pop()
                else:
                    stack.append(c)

            return "".join(stack)

        answer = getFinal(s) == getFinal(t)

        return answer


print(Solution().backspaceCompare(s="ab#c", t="ad#c") == True)
print(Solution().backspaceCompare(s="ab##", t="c#d#") == True)
print(Solution().backspaceCompare(s="a#c", t="b") == False)
