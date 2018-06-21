def solution(s):
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