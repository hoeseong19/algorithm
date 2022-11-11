def solution(s):
    answer = True

    stack = []

    for c in s:
        if c == '(':
            stack.append(c)

        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    answer = len(stack) == 0

    return answer


print(solution("()()") == True)
print(solution("(())()") == True)
print(solution(")()(") == False)
print(solution("(()(") == False)
