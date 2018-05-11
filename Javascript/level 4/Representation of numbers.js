function expressions(num) {
    var answer = 1;
    var tem = 0;
  for(var a=1; a<=num/2; a++){
  console.log("A",a)
      tem = a;
    for(var b=a+1; b<=num/2+1; b++){
    console.log("B",b)
      tem+=b;
        if(tem==num){
        answer++;
          break;
      }
    }
  }
return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(expressions(15));