s = input("Input = ") # 문자열 입력
new_s = "" # 새로운 문자열
stack = [] # stack

for i in range(len(s)): # stack push
    stack.append(s[i])

for _ in range(len(s)-1,-1,-1): # stack pop 후 문자열 중복 제거
    stack_s = stack.pop()
    if not stack_s in new_s:
        new_s += stack_s

print("Result: ", "".join(sorted(new_s))) # 문자열 정렬 후 출력