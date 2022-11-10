def solution(s):
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
            continue

        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return int(len(stack) == 0)


print(solution('baabaa') == 1)
print(solution('cdcd') == 0)
