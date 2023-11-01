import sys

n = int(sys.stdin.readline().rstrip())

answer = []
stack = []
for _ in range(n):
    list_input = sys.stdin.readline().rstrip().split()

    command = list_input[0]

    # 정수 X를 스택에 넣는 연산이다.
    if command == "push":
        stack.append(int(list_input[1]))
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if command == "pop":
        answer.append(-1 if len(stack) == 0 else stack.pop())
    # 스택에 들어있는 정수의 개수를 출력한다.
    if command == "size":
        answer.append(len(stack))
    # 스택이 비어있으면 1, 아니면 0을 출력한다.
    if command == "empty":
        answer.append(int(len(stack) == 0))
    # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if command == "top":
        answer.append(-1 if len(stack) == 0 else stack[-1])
for num in answer:
    print(num)

# with open("./baekjoon/10828/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         n = int(f.readline().rstrip())

#         answer = []
#         stack = []
#         for _ in range(n):
#             list_input = f.readline().rstrip().split()

#             command = list_input[0]

#             # 정수 X를 스택에 넣는 연산이다.
#             if command == "push":
#                 stack.append(int(list_input[1]))
#             # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#             if command == "pop":
#                 answer.append(-1 if len(stack) == 0 else stack.pop())
#             # 스택에 들어있는 정수의 개수를 출력한다.
#             if command == "size":
#                 answer.append(len(stack))
#             # 스택이 비어있으면 1, 아니면 0을 출력한다.
#             if command == "empty":
#                 answer.append(int(len(stack) == 0))
#             # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#             if command == "top":
#                 answer.append(-1 if len(stack) == 0 else stack[-1])

#         for num in answer:
#             print(num == int(f.readline().rstrip()))
