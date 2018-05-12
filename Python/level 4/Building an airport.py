def chooseCity(n,city):
    answer = 0
    sum = 0
    city = sorted(city, key=lambda city: city[0])
    
    for i in range(0,n):
        sum += city[i][1]
    
    half = sum / 2
    if half*2 != sum:
        half+=1
    sum = 0
    for i in range(0,n):
        sum += city[i][1]
        if sum >= half:
            break
    return city[i][0]

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,100],[10,98],[9,99]]))