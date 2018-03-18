function adder(a, b){
    var result = 0
    //함수를 완성하세요
    var tem;
    if(a>b){
    	tem = a;
      a = b;
      b = tem;
    }
    for(var i=a; i<=b;i++)
      result+=i;
    return result;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( adder(3, 5) )