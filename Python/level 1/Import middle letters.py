def string_middle(str):
    # 함수를 완성하세요
    tlen = len(str)
    if tlen % 2 == 1:
        return str[tlen//2]
    else:
        return str[tlen//2-1]+str[tlen//2]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))