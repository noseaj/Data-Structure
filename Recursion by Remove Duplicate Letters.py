def recursion(i):
    global new_s
    if i >= 0:
        recursion(i-1) # 이전 인덱스를 인수로 다시 함수 호출
        if i == 0: # 인덱스 0인 데이터 new_s에 대입
            new_s = s[i]
            return
        else: # 인덱스[i] 데이터가 new_s에 없으면 추가
            if not s[i] in new_s:
                new_s += s[i]
            return

s = input("Input = ") # 문자열 입력
new_s = "" # 새로운 문자열
recursion(len(s)-1) # 함수 호출
print("Result:  ", "".join(sorted(new_s))) # 문자열 정렬 후 출력