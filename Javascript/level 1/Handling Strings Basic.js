function alpha_string46(s){
  // 함수를 완성하세요
	if((s.length === 4 || s.length === 6) && !isNaN(s))
  	return true;
  return false;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( alpha_string46("a234") );