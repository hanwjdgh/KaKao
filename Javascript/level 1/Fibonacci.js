function fibonacci(num) {
	var answer = 0;
	var a =0;
  var b=1;
  for(var i=0; i<num; i++) {
        if(i != 0){
          answer = a + b;
          a = b;
          b = answer;
        }
  }
	return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(fibonacci(3))