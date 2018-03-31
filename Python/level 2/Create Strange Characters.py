def toWeirdCase(s):
    # 함수를 완성하세요
    list = s.split(" ")
    list2 = []
    for str in list:
        answer=""
        for tst in range(len(str)):
            if tst %2==0:
                answer+=str[tst].upper()
            else:
                answer+=str[tst].lower()
        list2.append(answer)
    
    return " ".join(list2)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));