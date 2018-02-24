function sumDivisor(num) {
	var answer = 0;
	for(var a =1; a<=num; a++){
  		if(num%a==0)
      	answer+=a;
  }
	return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(sumDivisor(12));