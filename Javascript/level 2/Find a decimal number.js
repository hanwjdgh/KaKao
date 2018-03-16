function numberOfPrime(n) {
	var result = 0;
	// 함수를 완성하세요.
	var cnt=0;
	for(var a=2;a<=n;a++){
    cnt=0;
  	for(var b=1;b<=a;b++){
    		if(a%b==0)
          cnt++;
    }
    if(cnt==2)
      result++;
  }
	return result;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( numberOfPrime(10) )