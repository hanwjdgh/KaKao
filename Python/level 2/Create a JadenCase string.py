def Jaden_Case(s):
    # 함수를 완성하세요
    list = s.split(" ")
    list2 = []
    for str in list:
        tem = ""
        for a in range(len(str)):
            if a==0:
                tem +=str[a].upper()
            else:
                tem+=str[a].lower()
        list2.append(tem)
    return " ".join(list2)        
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))